# Saints - Portal de Notícias de Tecnologia

## Sobre
Saints é um portal de notícias de tecnologia criado para manter profissionais e entusiastas atualizados sobre os principais acontecimentos em Inteligência Artificial, Startups, Segurança da Informação e Tecnologia em geral.
A aplicação coleta automaticamente notícias de fontes internacionais via RSS, extrai o conteúdo completo dos artigos e utiliza IA (LLaMA 3.3 70B via Groq) para reescrever e adaptar cada notícia para o português brasileiro, garantindo um conteúdo original, fluido e acessível ao público nacional.

## Tecnologias
**Backend**
- Python
- FastAPI
- SQLAlchemy
- SQLite
- APScheduler

**Frontend**
- HTML, CSS, JavaScript

**Integrações**
- Groq (LLaMA 3.3 70B)
- Feedparser (RSS)
- Newspaper3k (Web Scraping)

## Como rodar

### Backend
```bash
cd backend
source .venv/Scripts/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
python -m http.server 5500
```
Acesse: `http://localhost:5500/pages/home.html`

## Fluxo
RSS Feed → Web Scraping → IA reescreve → Banco de dados → API REST → Frontend