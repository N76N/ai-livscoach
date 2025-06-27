import secrets
import hashlib

def skapa_api_nyckel():
    return "sk-" + secrets.token_hex(32)

def hash_lösenord(lösenord):
    return hashlib.sha256(lösenord.encode()).hexdigest()