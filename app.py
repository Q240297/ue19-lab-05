import requests

def get_joke():
    # URL de l'API publique (blagues en anglais pour cet exemple)
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    
    try:
        response = requests.get(url)
        # Lève une erreur si la requête échoue (ex: 404, 500)
        response.raise_for_status()
        
        data = response.json()
        
        print("Voici une blague aléatoire pour vous :")
        print("--------------------------------------")
        # Affiche la blague ou un message par défaut
        print(data.get('joke', 'Aucune blague trouvée.'))
        print("--------------------------------------")
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la blague : {e}")

if __name__ == "__main__":
    get_joke()