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
        You are an experienced Brazilian technology journalist, specialized in rewriting news in a clear and engaging way.

        Based on this original title: "{article['title']}"
        And this original content: "{article['content']}"

        Generate exactly in this format:
        CATEGORY: {article['category']}
        TITLE: [rewritten title in Portuguese, objective and impactful]
        CONTENT: [complete news in Portuguese, professional tone, between 300 and 400 words, with introduction, development and conclusion]

        Rules:
        - Write only the title and content, no extra comments
        - Rewrite in your own words, do not copy the original content
        - Keep the facts and data present in the original content
        - Do not invent information that is not in the original content
        - All output must be in Portuguese (Brazilian)
        """

        response = client.responses.create(
            input=prompt,
            model="llama-3.3-70b-versatile")
        
        parsed = parse_news(response.output_text)

        news.append(parsed)

    return news

def parse_news(news):
    lines = news.split('\n')
    category = lines[0][10:]
    title = lines[1][7:]
    first_line = lines[3:][0][9:]
    rest = lines[4:]
    content = " ".join([first_line] + rest)
    return {'category':category,'title':title,'content':content}