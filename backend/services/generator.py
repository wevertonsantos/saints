from openai import OpenAI
from core.config import settings
from services.scraper import extract_articles

client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

def generate_news():
    articles = extract_articles()
    news = []

    for article in articles:
        prompt = f"""
        Você é um jornalista experiente de tecnologia brasileiro, especializado em reescrever notícias de forma clara e envolvente.

        Com base neste título original: "{article['title']}"
        E neste conteúdo original: "{article['content']}"

        Gere exatamente neste formato:
        CATEGORIA: {article['category']}
        TÍTULO: [título reescrito em português, objetivo e impactante]
        CONTEÚDO: [notícia completa em português, tom profissional, entre 300 a 400 palavras, com introdução, desenvolvimento e conclusão]

        Regras:
        - Escreva apenas o título e o conteúdo, sem comentários extras
        - Reescreva com suas próprias palavras, não copie o conteúdo original
        - Mantenha os fatos e dados presentes no conteúdo original
        - Não invente informações que não estejam no conteúdo original
        """

        response = client.responses.create(
            input=prompt,
            model="llama-3.3-70b-versatile")
        
        parsed = parse_news(response.output_text)

        news.append(parsed)

    return news

def parse_news(news):
    lines = news.split('\n')
    category = lines[0][11:]
    title = lines[1][8:]
    first_line = lines[3:][0][10:]
    rest = lines[4:]
    content = " ".join([first_line] + rest)
    return {'category':category,'title':title,'content':content}