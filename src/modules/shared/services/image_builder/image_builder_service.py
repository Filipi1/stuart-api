from PIL import Image, ImageDraw, ImageFont
import io
import base64
from typing import Optional
import os


class ImageBuilderService:
    FONT_NAME = "arial.ttf"
    
    def __init__(self):
        self.default_font_size = 16
        self.title_font_size = 32
        self.subtitle_font_size = 18
        self.header_font_size = 48
        self.info_font_size = 14
        self.max_width = 900
        self.max_height = 800
        
        self.margin = 50
        self.main_content_x_start = self.margin
        self.sidebar_x_start = self.max_width // 2 + self.margin
        self.main_content_width = self.sidebar_x_start - self.main_content_x_start - self.margin
        self.sidebar_width = self.max_width - self.sidebar_x_start - self.margin
        
        self.image_max_width = 400
        self.image_max_height = 300
    
    def create_fake_news_image(self, 
                             image_data: bytes, 
                             headline: str, 
                             subtitle: str = "",
                             frame_image_path: Optional[str] = None) -> str:
        try:
            received_image = Image.open(io.BytesIO(image_data))
            
            received_image = self._resize_image_to_fit(received_image)
            
            if frame_image_path and os.path.exists(frame_image_path):
                frame_image = Image.open(frame_image_path)
            else:
                frame_image = self._create_default_newspaper_frame()
            
            final_image = self._combine_images(frame_image, received_image, headline, subtitle)
            
            return self._image_to_base64(final_image)
            
        except Exception as e:
            raise ValueError(f"Erro ao processar imagem: {str(e)}")
    
    def _resize_image_to_fit(self, image: Image.Image) -> Image.Image:
        max_width = 400
        max_height = 300
        
        width_ratio = max_width / image.width
        height_ratio = max_height / image.height
        ratio = min(width_ratio, height_ratio)
        
        new_width = int(image.width * ratio)
        new_height = int(image.height * ratio)
        
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    def _create_default_newspaper_frame(self) -> Image.Image:
        frame = Image.new('RGB', (self.max_width, self.max_height), 'white')
        draw = ImageDraw.Draw(frame)
        
        draw.rectangle([0, 0, self.max_width-1, self.max_height-1], outline='black', width=2)
        
        self._draw_newspaper_header(draw)
        
        draw.line([(20, 120), (self.max_width-20, 120)], fill='black', width=1)
        draw.line([(20, 140), (self.max_width-20, 140)], fill='black', width=1)
        
        self._draw_current_date(draw)
        
        draw.line([(20, 180), (self.max_width-20, 180)], fill='black', width=1)
        
        self._draw_sidebar(draw)
        
        return frame
    
    def _draw_newspaper_header(self, draw: ImageDraw.Draw):
        try:
            header_font = ImageFont.truetype(self.FONT_NAME, self.header_font_size)
            info_font = ImageFont.truetype(self.FONT_NAME, self.info_font_size)
        except (OSError, IOError):
            header_font = ImageFont.load_default()
            info_font = ImageFont.load_default()
        
        newspaper_name = "STUART BAR"
        bbox = draw.textbbox((0, 0), newspaper_name, font=header_font)
        text_width = bbox[2] - bbox[0]
        x_position = (self.max_width - text_width) // 2
        draw.text((x_position, 20), newspaper_name, fill='black', font=header_font)
        
        edition_info = "Edição 2025 - Notícias"
        bbox = draw.textbbox((0, 0), edition_info, font=info_font)
        text_width = bbox[2] - bbox[0]
        x_position = (self.max_width - text_width) // 2
        draw.text((x_position, 80), edition_info, fill='black', font=info_font)
    
    def _draw_current_date(self, draw: ImageDraw.Draw):
        from datetime import datetime
        import locale
        
        try:
            locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        except (locale.Error, OSError):
            try:
                locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
            except (locale.Error, OSError):
                pass
        
        try:
            date_font = ImageFont.truetype(self.FONT_NAME, self.info_font_size)
        except (OSError, IOError):
            date_font = ImageFont.load_default()
        
        now = datetime.now()
        day_name = now.strftime("%A")
        day = now.strftime("%d")
        month_name = now.strftime("%B")
        year = now.strftime("%Y")
        
        day_names = {
            'Monday': 'Segunda-feira',
            'Tuesday': 'Terça-feira', 
            'Wednesday': 'Quarta-feira',
            'Thursday': 'Quinta-feira',
            'Friday': 'Sexta-feira',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo'
        }
        
        month_names = {
            'January': 'Janeiro',
            'February': 'Fevereiro',
            'March': 'Março',
            'April': 'Abril',
            'May': 'Maio',
            'June': 'Junho',
            'July': 'Julho',
            'August': 'Agosto',
            'September': 'Setembro',
            'October': 'Outubro',
            'November': 'Novembro',
            'December': 'Dezembro'
        }
        
        day_name_pt = day_names.get(day_name, day_name)
        month_name_pt = month_names.get(month_name, month_name)
        
        date_text = f"{day_name_pt}, {day} de {month_name_pt} de {year}"
        
        bbox = draw.textbbox((0, 0), date_text, font=date_font)
        text_width = bbox[2] - bbox[0]
        x_position = (self.max_width - text_width) // 2
        draw.text((x_position, 150), date_text, fill='black', font=date_font)
    
    def _draw_sidebar(self, draw: ImageDraw.Draw):
        try:
            sidebar_font = ImageFont.truetype(self.FONT_NAME, 12)
            title_font = ImageFont.truetype(self.FONT_NAME, 14)
        except (OSError, IOError):
            sidebar_font = ImageFont.load_default()
            title_font = ImageFont.load_default()
        
        sidebar_x = 500
        sidebar_width = self.max_width - sidebar_x - 20
        
        y_pos = 220
        draw.text((sidebar_x, y_pos), "EM DESTAQUE", fill='black', font=title_font)
        y_pos += 25
        
        draw.line([(sidebar_x, y_pos), (sidebar_x + sidebar_width, y_pos)], fill='black', width=1)
        y_pos += 15
        
        highlight_items = [
            "Novo esquema descoberto",
            "Políticos em apuros",
            "Escândalo na prefeitura",
            "Investigação avança"
        ]
        
        for item in highlight_items:
            draw.text((sidebar_x, y_pos), f"• {item}", fill='black', font=sidebar_font)
            y_pos += 20
        
        y_pos += 20
        draw.text((sidebar_x, y_pos), "EDITORIAL", fill='black', font=title_font)
        y_pos += 25
        
        draw.line([(sidebar_x, y_pos), (sidebar_x + sidebar_width, y_pos)], fill='black', width=1)
        y_pos += 15
        
        draw.text((sidebar_x, y_pos), "Por: Redação Stuart Bar", fill='black', font=sidebar_font)
        y_pos += 20
        
        editorial_lines = [
            "A verdade sempre vem à tona,",
            "mesmo quando tentam",
            "escondê-la. Nossa missão",
            "é trazer os fatos para",
            "nossos leitores."
        ]
        
        for line in editorial_lines:
            draw.text((sidebar_x, y_pos), line, fill='black', font=sidebar_font)
            y_pos += 15
    
    def _combine_images(self, frame: Image.Image, content_image: Image.Image, headline: str, subtitle: str = "") -> Image.Image:
        result = frame.copy()
        draw = ImageDraw.Draw(result)

        x_offset = self.main_content_x_start + (self.main_content_width - content_image.width) // 2
        y_offset = 220
        
        result.paste(content_image, (x_offset, y_offset))
        
        headline_y = y_offset + content_image.height + 20
        self._add_headline(draw, headline, headline_y)
        
        if subtitle:
            title_height = self._calculate_text_height(draw, headline, self.title_font_size)
            subtitle_y = headline_y + title_height + 10
            self._add_subtitle(draw, subtitle, subtitle_y)
        
        return result
    
    def _calculate_text_height(self, draw: ImageDraw.Draw, text: str, font_size: int) -> int:
        font = self._get_font(font_size)
        lines = self._wrap_text(draw, text, font, self.main_content_width)
        return len(lines) * (font_size + 5)
    
    def _add_headline(self, draw: ImageDraw.Draw, headline: str, y_position: int):
        font = self._get_font(self.title_font_size)
        lines = self._wrap_text(draw, headline, font, self.main_content_width)
        self._draw_text_lines(draw, lines, font, y_position, self.title_font_size, self.main_content_x_start, self.main_content_width, bold=True)
    
    def _get_font(self, size: int) -> ImageFont.ImageFont:
        try:
            return ImageFont.truetype(self.FONT_NAME, size)
        except (OSError, IOError) as e:
            print(f"Aviso: Não foi possível carregar a fonte {self.FONT_NAME}: {e}")
            return ImageFont.load_default()
    
    def _wrap_text(self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            test_line = ' '.join(current_line)
            bbox = draw.textbbox((0, 0), test_line, font=font)
            text_width = bbox[2] - bbox[0]
            
            if text_width > max_width:
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
                    current_line = []
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def _draw_text_lines(self, draw: ImageDraw.Draw, lines: list[str], font: ImageFont.ImageFont, 
                        y_position: int, line_height: int, x_start_position: int, max_text_width: int, bold: bool = False, color: str = 'black'):
        for i, line in enumerate(lines):
            y_pos = y_position + (i * (line_height + 5))
            self._draw_single_text_line(draw, line, font, y_pos, x_start_position, max_text_width, bold, color)
    
    def _draw_single_text_line(self, draw: ImageDraw.Draw, line: str, font: ImageFont.ImageFont, 
                              y_pos: int, x_start_position: int, max_text_width: int, bold: bool = False, color: str = 'black'):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x_position = x_start_position + (max_text_width - text_width) // 2
        
        if bold:
            self._draw_bold_text(draw, line, font, x_position, y_pos, color)
        else:
            draw.text((x_position, y_pos), line, fill=color, font=font)
    
    def _draw_bold_text(self, draw: ImageDraw.Draw, line: str, font: ImageFont.ImageFont, 
                       x_position: int, y_pos: int, color: str = 'black'):
        for offset_x in range(-1, 2):
            for offset_y in range(-1, 2):
                if offset_x != 0 or offset_y != 0:
                    draw.text((x_position + offset_x, y_pos + offset_y), line, fill=color, font=font)
        
        draw.text((x_position, y_pos), line, fill=color, font=font)
    
    def _add_subtitle(self, draw: ImageDraw.Draw, subtitle: str, y_position: int):
        font = self._get_font(self.subtitle_font_size)
        lines = self._wrap_text(draw, subtitle, font, self.main_content_width)
        self._draw_text_lines(draw, lines, font, y_position, self.subtitle_font_size, self.main_content_x_start, self.main_content_width, bold=False, color='darkgray')
    
    def _image_to_base64(self, image: Image.Image) -> str:
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG', quality=85)
        buffer.seek(0)
        return base64.b64encode(buffer.getvalue()).decode('utf-8')
