# Stuart API - Arquitetura e Padrões para Cursor

## Visão Geral da Arquitetura

Este projeto segue uma **arquitetura hexagonal (Clean Architecture)** com **Domain-Driven Design (DDD)**, organizando o código em módulos de domínio com separação clara de responsabilidades.

## Estrutura de Diretórios

```
src/
├── main.py                          # Ponto de entrada da aplicação
└── modules/                         # Módulos de domínio
    ├── shared/                      # Código compartilhado
    │   ├── adapters/               # Adaptadores base (Repository, Service, Controller)
    │   ├── decorators/             # Decorators customizados (@API.controller, @API.route)
    │   ├── middleware/             # Middlewares (Correlation ID, CORS)
    │   ├── services/               # Serviços compartilhados (Logger, Supabase)
    │   ├── settings/               # Configurações (Settings com Pydantic)
    │   └── utils/                  # Utilitários compartilhados
    └── {domain}/                   # Módulos de domínio (album, auth, coach, meme, user)
        ├── controllers/            # Controladores da API
        ├── dtos/                   # Data Transfer Objects (Request/Response)
        ├── entities/               # Entidades de domínio
        ├── exceptions/             # Exceções específicas do domínio
        ├── providers/              # Providers de injeção de dependência
        ├── repositories/           # Repositórios de dados
        └── services/               # Serviços de aplicação e domínio
            ├── application/        # Serviços de aplicação (orquestração)
            └── domain/             # Serviços de domínio (regras de negócio)
```

## Padrões Arquiteturais Identificados

### 1. **Clean Architecture / Hexagonal Architecture**
- **Controllers**: Interface com a API (camada externa)
- **Application Services**: Orquestração de casos de uso
- **Domain Services**: Regras de negócio puras
- **Repositories**: Acesso a dados (infraestrutura)
- **Entities**: Objetos de domínio

### 2. **Domain-Driven Design (DDD)**
- Módulos organizados por domínio de negócio
- Entidades com comportamento e validação
- Serviços de domínio para regras complexas
- Exceções específicas por domínio

### 3. **Dependency Injection**
- Providers para injeção de dependência
- Uso de `Annotated` e `Depends` do FastAPI
- Inversão de dependência através de abstrações

### 4. **Decorator Pattern**
- `@API.controller`: Decorator para controladores
- `@API.route`: Decorator para rotas da API
- Auto-descoberta de controladores

## Convenções de Código

### **Nomenclatura**
- **Controllers**: `{Domain}Controller` (ex: `AlbumController`)
- **Services**: `{Action}{Domain}Service` (ex: `FetchAlbumApplicationService`)
- **Entities**: `{Domain}Entity` (ex: `MemeEntity`)
- **DTOs**: `{Action}{Domain}RequestDto/ResponseDto`
- **Repositories**: `{Domain}Repository` (ex: `MemeRepository`)
- **Providers**: `{Service}Provider` (ex: `FetchAlbumServiceProvider`)

### **Estrutura de Arquivos**
- Cada módulo de domínio segue a mesma estrutura
- DTOs organizados por ação em subpastas
- Services separados em `application/` e `domain/`
- Providers centralizam a injeção de dependência

### **Padrões de Implementação**

#### **Controllers**
```python
@API.controller("domain")
class DomainController(APIController):
    @API.route("/", method=HTTPMethod.GET)
    async def get_domain(
        self,
        service: ServiceProvider,
        param: str = Query(...)
    ):
        return await service.process(RequestDto(param=param))
```

#### **Application Services**
```python
class DomainApplicationService(ApplicationService):
    def __init__(self, domain_service: DomainService, repository: Repository):
        self.__domain_service = domain_service
        self.__repository = repository
        super().__init__(self.__class__.__name__)

    async def process(self, input: RequestDto) -> ResponseDto:
        # Orquestração de casos de uso
        result = await self.__domain_service.process(input)
        return ResponseDto(data=result)
```

#### **Domain Services**
```python
class DomainDomainService(DomainService):
    def process(self, input: RequestDto) -> Entity:
        # Regras de negócio puras
        return processed_entity
```

#### **Repositories**
```python
class DomainRepository(RepositoryAdapter):
    def __init__(self, supabase_service: SupabaseService):
        self.__supabase_service = supabase_service
        super().__init__("table_name")

    async def get_by_id(self, id: int) -> Entity:
        response = await self.__supabase_service.read(self.table, {"id": id})
        return Entity(**response[0]) if response else None
```

#### **Providers**
```python
def service_provider(
    dependency1: Dependency1Provider,
    dependency2: Dependency2Provider,
):
    return Service(
        dependency1=dependency1,
        dependency2=dependency2,
    )

ServiceProvider = Annotated[Service, Depends(service_provider)]
```

## Tecnologias e Ferramentas

### **Backend**
- **FastAPI**: Framework web assíncrono
- **Pydantic**: Validação de dados e serialização
- **Supabase**: Backend-as-a-Service (banco de dados)
- **Loguru**: Sistema de logging avançado
- **Pillow**: Processamento de imagens

### **Desenvolvimento**
- **UV**: Gerenciador de dependências Python
- **Ruff**: Linter e formatter
- **Black**: Formatter de código
- **Pyright**: Type checker
- **Taskipy**: Gerenciador de tarefas

### **Arquitetura**
- **Clean Architecture**: Separação de responsabilidades
- **DDD**: Design orientado a domínio
- **Dependency Injection**: Inversão de controle
- **Repository Pattern**: Abstração de acesso a dados
- **Service Layer**: Camada de serviços

## Middleware e Recursos Compartilhados

### **Correlation ID**
- Middleware para rastreamento de requests
- Context variable para acesso global
- Headers de resposta com ID de correlação

### **Logger Service**
- Logging estruturado com cores
- Integração com correlation ID
- Métodos auxiliares (title_box, dict_to_table)

### **Supabase Service**
- Cliente assíncrono para Supabase
- Operações CRUD genéricas
- Upload de arquivos para storage
- Queries customizadas com filtros

## Regras para Cursor

### **Ao criar novos módulos:**
1. Siga a estrutura de diretórios estabelecida
2. Crie controllers, services, repositories e providers
3. Use os decorators `@API.controller` e `@API.route`
4. Implemente DTOs para entrada e saída
5. Crie exceções específicas do domínio

### **Ao implementar funcionalidades:**
1. Comece pelas entidades de domínio
2. Implemente os repositórios
3. Crie os serviços de domínio
4. Desenvolva os serviços de aplicação
5. Configure os providers de injeção
6. Implemente os controllers

### **Padrões obrigatórios:**
- Use `ApplicationService` para orquestração
- Use `DomainService` para regras de negócio
- Use `RepositoryAdapter` para acesso a dados
- Use `APIController` para controladores
- Implemente logging em todos os serviços
- Use DTOs para comunicação entre camadas

### **Convenções de código:**
- Nomes em inglês para código
- Comentários e logs em português
- Type hints obrigatórios
- Validação com Pydantic
- Tratamento de exceções específicas

Esta arquitetura garante **manutenibilidade**, **testabilidade** e **escalabilidade** através da separação clara de responsabilidades e inversão de dependências.
