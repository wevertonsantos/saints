from openai import OpenAI

from core.config import settings

from services.scraper import extract_articles

from openai import RateLimitError

client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

def generate_news():
    articles = extract_articles()
    url = ''
    news = []

    for article in articles:
        url = article['url']
        prompt = f"""
        You are an experienced Brazilian technology journalist, specialized in rewriting news in a clear and engaging way.

        Based on this original title: "{article['title']}"
        And this original content: "{article['content']}"

        Generate exactly in this format (use these exact labels in English):
        CATEGORY: {article['category']}
        TITLE: [rewritten title in Portuguese]
        CONTENT: [complete news in Portuguese, between 300 and 400 words]

        Rules:
        - Write only the title and content, no extra comments
        - Rewrite in your own words, do not copy the original content
        - Keep the facts and data present in the original content
        - Do not invent information that is not in the original content
        - All output must be in Portuguese (Brazilian)
        """

        try:
            response = client.responses.create(
                input=prompt,
                model="llama-3.3-70b-versatile")
            parsed = parse_news(response.output_text,url)
            news.append(parsed)
        except RateLimitError:
            print("Rate limit reached, please try again later.")
            break
        except Exception as e:
            print(f'Error generating news item: {e}')
            continue
        
    return news

def parse_news(news,url):
    parts = news.split("TITLE:")
    category = parts[0].replace("CATEGORY:", "").strip()

    title_and_content = parts[1].split("CONTENT:")
    title = title_and_content[0].strip()
    content = title_and_content[1].strip()

    return {'url':url,'category':category,'title':title,'content':content}