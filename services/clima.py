import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def consultar_clima(cidade):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={cidade}"
        f"&appid={API_KEY}"
        f"&units=metric"
        f"&lang=pt_br"
    )

    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        return None
    
    dados = resposta.json()
    
    return {
        "cidade": dados["name"],
        "temperatura": dados["main"]["temp"],
        "sensacao": dados["main"]["feels_like"],
        "umidade": dados["main"]["humidity"],
        "condicao": dados["weather"][0]["description"]
    }
