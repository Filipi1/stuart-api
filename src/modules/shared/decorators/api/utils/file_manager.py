import inspect
import os
import sys
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import List


@dataclass
class FileEntity:
    name: str
    path: str


class FileManager:
    @staticmethod
    def _get_search_path() -> str:
        """Determina o caminho base para busca de arquivos."""
        # Tenta usar PYTHONPATH primeiro (configurado no Docker como /app/src)
        pythonpath = os.environ.get("PYTHONPATH")
        if pythonpath:
            # Se PYTHONPATH aponta para src/, usa o diretório pai
            if pythonpath.endswith("/src") or pythonpath.endswith("\\src"):
                return str(Path(pythonpath).parent)
            return pythonpath
        
        # Se não houver PYTHONPATH, usa o diretório do arquivo atual
        # e sobe até encontrar o diretório raiz do projeto
        current_file = Path(__file__).resolve()
        # Sobe do arquivo atual até encontrar o diretório que contém 'src'
        for parent in current_file.parents:
            src_dir = parent / "src"
            if src_dir.exists() and src_dir.is_dir():
                return str(parent)
        
        # Fallback para o diretório de trabalho atual
        return os.getcwd()

    @staticmethod
    def find_files_in_project(end_with: str) -> List[FileEntity]:
        files: List[FileEntity] = []
        path = FileManager._get_search_path()
        for root, _, finded_files in os.walk(path):
            # Ignora diretórios que não devem ser pesquisados
            if any(ignored in root for ignored in ['.venv', '__pycache__', '.git', 'node_modules']):
                continue
            for file in finded_files:
                if file.endswith(end_with):
                    file_entity = FileEntity(name=file, path=os.path.join(root, file))
                    files.append(file_entity)
        return files

    @staticmethod
    def _path_to_module_name(file_path: str, search_path: str) -> str:
        """Converte um caminho de arquivo para um nome de módulo Python."""
        file_path = Path(os.path.normpath(file_path))
        search_path = Path(os.path.normpath(search_path))
        
        # Remove a extensão .py
        if file_path.suffix == '.py':
            file_path = file_path.with_suffix('')
        
        # Determina o diretório src/
        pythonpath = os.environ.get("PYTHONPATH")
        if pythonpath:
            src_dir = Path(pythonpath)
        else:
            # Procura por src/ no caminho do arquivo ou no search_path
            src_dir = None
            for part in file_path.parts:
                if part == 'src':
                    idx = file_path.parts.index('src')
                    src_dir = Path(*file_path.parts[:idx+1])
                    break
            
            if not src_dir:
                src_dir = search_path / "src" if (search_path / "src").exists() else search_path
        
        # Calcula o caminho relativo a partir de src/
        try:
            relative_path = file_path.relative_to(src_dir)
        except ValueError:
            # Tenta encontrar src/ no caminho do arquivo
            parts = file_path.parts
            if 'src' in parts:
                idx = parts.index('src')
                relative_path = Path(*parts[idx+1:])
            else:
                return None
        
        # Converte para nome de módulo
        module_name = str(relative_path).replace(os.sep, '.').replace('/', '.').replace('\\', '.')
        return module_name

    @staticmethod
    def get_file_class_instance(
        file_entity: FileEntity, match_class: type
    ) -> list:
        instances = []
        search_path = FileManager._get_search_path()
        module_name = FileManager._path_to_module_name(file_entity.path, search_path)
        
        if not module_name:
            return instances
        
        try:
            # Garante que o diretório src está no sys.path
            pythonpath = os.environ.get("PYTHONPATH")
            if pythonpath and pythonpath not in sys.path:
                sys.path.insert(0, pythonpath)
            elif not pythonpath:
                # Tenta adicionar o diretório src ao sys.path
                search_path_obj = Path(search_path)
                src_path = search_path_obj / "src" if (search_path_obj / "src").exists() else search_path_obj
                if str(src_path) not in sys.path:
                    sys.path.insert(0, str(src_path))
            
            # Importa o módulo
            module = import_module(module_name)
            
            # Procura por classes Controller no módulo
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name == match_class.__name__:
                    continue
                if name.endswith("Controller") and issubclass(obj, match_class):
                    instances.append(obj())
        except Exception:
            # Silenciosamente ignora erros de importação
            # (pode ser um arquivo que não é um controller válido)
            pass
        
        return instances
