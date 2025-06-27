# AI Livscoach (MVP)

En FastAPI-baserad backend som erbjuder inloggning och AI-coachning med GPT-4.

## Funktioner
- `/signup` – Skapa användare
- `/login` – Logga in och få API-nyckel
- `/dagens-tips` – Få ett dagligt tips från en AI-livscoach (kräver API-nyckel)

## Starta lokalt

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Öppna sedan: http://127.0.0.1:8000/docs