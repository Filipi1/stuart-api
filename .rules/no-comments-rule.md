# Regra: Evitar Comentários Desnecessários

## Objetivo
Manter o código limpo e legível sem comentários óbvios ou desnecessários.

## Diretrizes

### ❌ NÃO adicionar comentários para:
- Explicar código óbvio
- Descrever o que o código faz quando é autoexplicativo
- Comentários redundantes que apenas repetem o código
- Comentários de seção óbvias

### ✅ Comentários permitidos apenas para:
- Explicar lógica complexa ou não óbvia
- Documentar decisões de design importantes
- Explicar algoritmos complexos
- Documentar APIs públicas
- Avisos importantes sobre comportamento

## Exemplos

### ❌ Ruim:
```python
# Incrementa o contador
counter += 1

# Retorna o resultado
return result

# Cria uma nova instância
instance = MyClass()
```

### ✅ Bom:
```python
counter += 1
return result
instance = MyClass()
```

### ✅ Comentário útil:
```python
# Usa algoritmo de ordenação O(n log n) para grandes datasets
sorted_data = merge_sort(large_dataset)

# Fallback para quando a fonte do sistema não está disponível
except (OSError, IOError):
    font = ImageFont.load_default()
```

## Aplicação
- Aplicar em todos os arquivos Python
- Priorizar código autoexplicativo
- Usar nomes de variáveis e funções descritivos
- Manter comentários apenas quando realmente necessário
