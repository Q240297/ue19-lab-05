import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        print("-------------------------------")
        print("Voici une blague pour le labo :")
        print(data.get('joke', 'No joke found.'))
        print("-------------------------------")
        
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    get_joke()