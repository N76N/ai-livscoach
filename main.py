from fastapi import FastAPI, HTTPException, Request
from models import SignupModel, LoginModel
from auth import skapa_api_nyckel, hash_lösenord
from db import users, api_keys
from coach import generera_coachtips

app = FastAPI()

@app.post("/signup")
def signup(data: SignupModel):
    if data.email in users:
        raise HTTPException(status_code=400, detail="Användaren finns redan")

    nyckel = skapa_api_nyckel()
    users[data.email] = {
        "password": hash_lösenord(data.lösenord),
        "api_key": nyckel
    }
    api_keys[nyckel] = data.email
    return {"meddelande": "Konto skapat", "din_api_nyckel": nyckel}

@app.post("/login")
def login(data: LoginModel):
    user = users.get(data.email)
    if not user or user["password"] != hash_lösenord(data.lösenord):
        raise HTTPException(status_code=401, detail="Fel e-post eller lösenord")
    return {"meddelande": "Inloggning lyckades", "din_api_nyckel": user["api_key"]}

@app.get("/dagens-tips")
def dagens_tips(request: Request):
    api_key = request.headers.get("x-api-key")
    if not api_key or api_key not in api_keys:
        raise HTTPException(status_code=401, detail="Ogiltig eller saknad API-nyckel")
    return {"tips": generera_coachtips("Vad är ett tips för att få bättre balans idag?")}