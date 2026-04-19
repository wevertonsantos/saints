# Saints — Portal de Notícias de Tecnologia

## 📖 Sobre

Saints é um portal de notícias de tecnologia criado para manter profissionais e entusiastas atualizados sobre os principais acontecimentos em Inteligência Artificial, Startups, Segurança da Informação e Tecnologia em geral.

A aplicação coleta automaticamente notícias de fontes internacionais via RSS, extrai o conteúdo completo dos artigos e utiliza IA (LLaMA 3.3 70B via Groq) para reescrever e adaptar cada notícia para o português brasileiro — garantindo conteúdo original, fluido e acessível ao público nacional.

---

## 🚀 Tecnologias

### Backend
| Tecnologia | Descrição |
|---|---|
| Python | Linguagem principal |
| FastAPI | Framework da API REST |
| SQLAlchemy | ORM para banco de dados |
| SQLite | Banco de dados |
| APScheduler | Agendamento de tarefas |

### Frontend
| Tecnologia | Descrição |
|---|---|
| HTML | Estrutura |
| CSS | Estilização |
| JavaScript | Interatividade |

### Integrações
| Integração | Descrição |
|---|---|
| Groq (LLaMA 3.3 70B) | Geração e reescrita de notícias com IA |
| Feedparser | Consumo de feeds RSS |
| Newspaper3k | Web scraping de artigos |

---

## ⚙️ Como rodar

### Pré-requisitos
- Python 3.9+
- Git

### Backend
```bash
cd backend
source .venv/Scripts/activate  # Windows (Git Bash)
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
python -m http.server 5500
```

Acesse: `http://localhost:5500/pages/home.html`

---

## 🔄 Fluxo da Aplicação
RSS Feed → Web Scraping → IA (Groq) → Banco de dados → API REST → Frontend

---

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na pasta `backend` com base no `.env.example`:

```env
DATABASE_URL=sqlite:///./database.db

GROQ_API_KEY=sua_key_aqui

RSS_URL=https://www.site.com/rss/index.xml
RSS_TAGS=

ALLOWED_ORIGINS=https://localhost:3000,https://localhost:5173,http://127.0.0.1:5500,http://localhost:5500,http://127.0.0.1:8000

API_PREFIX=/api

DEBUG=True
```