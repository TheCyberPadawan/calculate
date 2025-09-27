import requests
import json

API_TOKEN = "97a405f1664a83329a7d89ebf51dc227b90633c4ba4a2575"
BASE_URL = "https://api.pappers.fr/v2/recherche"

ASCII_ART = r"""
 /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$ 
| $$__  $$ /$$__  $$| $$__  $$| $$_____/| $$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$| $$  \__/
| $$$$$$$/| $$$$$$$$| $$$$$$$/| $$$$$   | $$$$$$$/|  $$$$$$ 
| $$____/ | $$__  $$| $$____/ | $$__/   | $$__  $$ \____  $$
| $$      | $$  | $$| $$      | $$      | $$  \ $$ /$$  \ $$
| $$      | $$  | $$| $$      | $$$$$$$$| $$  | $$|  $$$$$$/
|__/      |__/  |__/|__/      |________/|__/  |__/ \______/ 
"""

def search_pappers(query: str):
    """Envoie une requête à l'API Pappers avec le paramètre q."""
    params = {
        "q": query,
        "api_token": API_TOKEN,
        "precision": "standard",
        "bases": "entreprises,dirigeants,publications",
        "page": 1,
        "par_page": 5,  # on limite à 5 résultats pour pas flooder
        "case_sensitive": "false"
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    response = requests.get(BASE_URL, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Erreur {response.status_code}: {response.text}")

if __name__ == "__main__":
    print(ASCII_ART)
    print("🔎 Bienvenue sur Papers CLI")
    while True:
        name = input("\nEntrez un nom à rechercher (ou 'quit' pour sortir) : ").strip()
        if name.lower() in ["quit", "exit"]:
            print("👋 Au revoir !")
            break
        search_pappers(name)
