"""
Script de teste para o módulo de fakenews
"""
import asyncio
import io
from fastapi import UploadFile
from modules.fakenews.controllers.fake_news_controller import FakeNewsController


async def test_fake_news():
    """Testa a funcionalidade de criação de notícias falsas"""
    
    # Cria uma imagem de teste simples (1x1 pixel vermelho)
    test_image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\nIDATx\x9cc\xf8\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00IEND\xaeB`\x82'
    
    # Cria um UploadFile simulado
    test_image_file = UploadFile(
        file=io.BytesIO(test_image_data),
        filename="test_image.png",
        content_type="image/png"
    )
    
    # Cria o controller
    controller = FakeNewsController()
    
    try:
        # Testa a criação da notícia falsa
        response = await controller.create_fake_news(
            name="Diego",
            image=test_image_file
        )
        print("✅ Teste passou! Notícia falsa criada com sucesso.")
        print(f"ID: {response.content['id']}")
        print(f"Nome: {response.content['name']}")
        print(f"Manchete: {response.content['headline']}")
        print(f"Imagem base64 gerada: {len(response.content['image_base64'])} caracteres")
        print("\n🎨 Layout melhorado inclui:")
        print("- Cabeçalho 'Stuart Bar'")
        print("- Data atual em português")
        print("- Sidebar com 'Em destaque' e 'Editorial'")
        print("- Imagem redimensionada (400x300px)")
        print("- Subtítulo posicionado abaixo do título")
        
    except Exception as e:
        print(f"❌ Teste falhou: {str(e)}")


if __name__ == "__main__":
    asyncio.run(test_fake_news())
