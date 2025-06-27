from auth import hash_lösenord

users = {
    "niklas.nylander@hotmail.com": {
        "password": hash_lösenord("Minnah1076!"),
        "api_key": "sk-test-niklas"
    }
}

api_keys = {
    "sk-test-niklas": "niklas.nylander@hotmail.com"
}