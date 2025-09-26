# Módulo FakeNews

Este módulo é responsável por criar notícias falsas de forma divertida, combinando uma imagem enviada pelo usuário com uma manchete aleatória e um frame de jornal fictício com layout profissional.

## Funcionalidades

- **Layout Realista de Jornal**: Cria um layout profissional com cabeçalho "Stuart Bar", data atual e formatação de jornal
- **Sidebar Completa**: Inclui seções "Em destaque" e "Editorial" no lado direito
- **Geração de Manchetes Aleatórias**: Cria manchetes engraçadas e "ousadas" baseadas no nome fornecido
- **Subtítulos Automáticos**: Gera subtítulos complementares posicionados abaixo do título
- **Processamento de Imagem**: Redimensiona e integra a imagem enviada (400x300px) no layout
- **Data Atual**: Inclui a data atual formatada em português brasileiro
- **Retorno em Base64**: A imagem final é retornada em formato base64 para fácil integração

## Estrutura

```
fakenews/
├── controllers/
│   └── fake_news_controller.py    # Controller com endpoints
├── dtos/
│   └── create_fake_news/          # DTOs de requisição e resposta
├── entities/
│   └── fake_news.py              # Entidade FakeNews
├── services/
│   ├── application/              # Serviços de aplicação
│   └── domain/                   # Serviços de domínio
└── test_fake_news.py            # Script de teste
```

## Endpoints

### POST /v1/fakenews/

Cria uma notícia falsa com base na imagem e nome fornecidos.

**Request (Form-Data):**
- `name` (string): Nome da pessoa para incluir na manchete
- `image` (file): Arquivo de imagem (PNG, JPG, JPEG, etc.)

**Exemplo de uso com curl:**
```bash
curl -X POST "http://localhost:8000/v1/fakenews/" \
  -F "name=Diego" \
  -F "image=@caminho/para/imagem.jpg"
```

**Response:**
```json
{
  "id": "uuid-gerado",
  "name": "Diego",
  "headline": "Descobrimos o paradeiro do vendedor de calsinhas, saiba mais como Diego fazia seus esquemas",
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAA...",
  "created_at": "2024-01-01T12:00:00"
}
```

**Imagem Gerada:**
A imagem retornada inclui:
- **Cabeçalho**: "STUART BAR" em destaque
- **Informações**: "Edição 2025 - Notícias"
- **Data atual**: "Segunda-feira, 22 de Janeiro de 2025"
- **Imagem principal**: Redimensionada para 400x300px (lado esquerdo)
- **Manchete principal**: Em destaque e negrito
- **Subtítulo**: Posicionado abaixo do título
- **Sidebar**: Seções "Em destaque" e "Editorial" (lado direito)

## Layout da Imagem

```
┌─────────────────────────────────────────────────────────┐
│                    STUART BAR                          │
│                Edição 2025 - Notícias                  │
│ ─────────────────────────────────────────────────────── │
│        Segunda-feira, 22 de Janeiro de 2025           │
│ ─────────────────────────────────────────────────────── │
│                                                         │
│  [IMAGEM 400x300]        │  EM DESTAQUE                │
│                          │  ──────────                 │
│                          │  • Novo esquema descoberto  │
│                          │  • Políticos em apuros      │
│                          │  • Escândalo na prefeitura  │
│                          │  • Investigação avança      │
│                          │                             │
│                          │  EDITORIAL                  │
│                          │  ──────────                 │
│                          │  Por: Redação Stuart Bar    │
│                          │  A verdade sempre vem à     │
│                          │  tona, mesmo quando tentam  │
│                          │  escondê-la. Nossa missão   │
│                          │  é trazer os fatos para     │
│                          │  nossos leitores.           │
│                                                         │
│     MANCHETE PRINCIPAL                                  │
│        Subtítulo complementar                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Exemplo de Uso

### Com Python (usando requests)
```python
import requests

url = "http://localhost:8000/v1/fakenews/"
files = {"image": open("imagem.jpg", "rb")}
data = {"name": "Diego"}

response = requests.post(url, files=files, data=data)
result = response.json()
print(f"Manchete: {result['headline']}")
```

### Com curl
```bash
curl -X POST "http://localhost:8000/v1/fakenews/" \
  -F "name=Diego" \
  -F "image=@imagem.jpg"
```

### Com JavaScript (fetch)
```javascript
const formData = new FormData();
formData.append('name', 'Diego');
formData.append('image', fileInput.files[0]);

fetch('/v1/fakenews/', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

## Dependências

- **PIL (Pillow)**: Para processamento de imagens
- **FastAPI**: Para endpoints da API
- **base64**: Para codificação/decodificação de imagens
- **uuid**: Para geração de IDs únicos
- **datetime**: Para timestamps

## Notas

- O módulo gera manchetes aleatórias de uma lista pré-definida
- As imagens são redimensionadas para 400x300px para melhor proporção
- O layout inclui sidebar com conteúdo realista de jornal
- Subtítulos são posicionados automaticamente abaixo dos títulos
- Todas as imagens são retornadas em formato JPEG com qualidade 85%
