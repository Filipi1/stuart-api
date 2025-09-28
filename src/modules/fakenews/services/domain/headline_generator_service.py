import random
from typing import List


class HeadlineGeneratorService:
    """Serviço responsável por gerar manchetes aleatórias para notícias falsas"""

    def __init__(self):
        self.headline_templates = [
            "Descobrimos o paradeiro do vendedor de calsinhas, saiba mais como {name} fazia seus esquemas",
            "Exclusivo: {name} é flagrado em situação constrangedora, veja as imagens",
            "Polêmica: {name} causa revolta nas redes sociais com declaração polêmica",
            "Escândalo: {name} é descoberto em esquema milionário, autoridades investigam",
            "Bomba: {name} revela segredo que pode mudar tudo, confira os detalhes",
            "Chocante: {name} é pego em flagrante, população fica em choque",
            "Exclusivo: {name} admite crime em entrevista surpresa",
            "Polêmica: {name} causa polêmica com atitude inesperada",
            "Escândalo: {name} é descoberto em situação inusitada",
            "Bomba: {name} revela informação que ninguém esperava",
            "Chocante: {name} é flagrado em atitude que chocou a todos",
            "Exclusivo: {name} admite verdade que ninguém sabia",
            "Polêmica: {name} causa revolta com declaração inesperada",
            "Escândalo: {name} é descoberto em esquema que ninguém imaginava",
            "Bomba: {name} revela segredo que pode mudar tudo",
            "Chocante: {name} é pego em flagrante em situação inusitada",
            "Exclusivo: {name} admite crime que ninguém esperava",
            "Polêmica: {name} causa polêmica com atitude que chocou a todos",
            "Escândalo: {name} é descoberto em situação que ninguém imaginava",
            "Bomba: {name} revela informação que pode mudar tudo",
        ]

        self.subtitle_templates = [
            "Subtítulo curto que complementa a manchete e resume o ponto principal",
            "Investigação revela detalhes surpreendentes sobre o caso",
            "Especialistas analisam as implicações da descoberta",
            "Comunidade local reage com surpresa às notícias",
            "Autoridades prometem investigação completa do caso",
            "Fonte próxima revela informações exclusivas",
            "Testemunhas confirmam os fatos relatados",
            "Análise detalhada mostra como tudo aconteceu",
            "Especialistas explicam o significado da descoberta",
            "População local comenta sobre as revelações",
        ]

    def generate_headline(self, name: str) -> tuple[str, str]:
        """
        Gera uma manchete e subtítulo aleatórios baseados no nome fornecido

        Args:
            name: Nome da pessoa para incluir na manchete

        Returns:
            Tupla com (manchete, subtítulo)
        """
        headline_template = random.choice(self.headline_templates)
        subtitle_template = random.choice(self.subtitle_templates)

        headline = headline_template.format(name=name)
        subtitle = subtitle_template

        return headline, subtitle

    def generate_multiple_headlines(self, name: str, count: int = 3) -> List[str]:
        """
        Gera múltiplas manchetes aleatórias para o mesmo nome

        Args:
            name: Nome da pessoa para incluir nas manchetes
            count: Número de manchetes para gerar

        Returns:
            Lista de strings com as manchetes geradas
        """
        headlines = []
        used_templates = set()

        while len(headlines) < count and len(used_templates) < len(
            self.headline_templates
        ):
            template = random.choice(self.headline_templates)
            if template not in used_templates:
                headlines.append(template.format(name=name))
                used_templates.add(template)

        return headlines
