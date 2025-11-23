# Générateur de Blagues Python

Application Python 3 simple qui interroge l'API publique [JokesAPI](https://v2.jokeapi.dev/) pour afficher une blague aléatoire. Ce projet fait partie du laboratoire `ue19-lab-05`.

## Fichiers
* `app.py` : Le script principal qui interroge l'API.
* `requirements.txt` : Liste des dépendances (librairie requests).
* `Dockerfile` : Instructions pour construire l'image Docker.

## Installation et exécution (Localement)

1.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Lancer le script :**
    ```bash
    python app.py
    ```

## Utilisation avec Docker

1.  **Construire l'image :**
    ```bash
    docker build -t python-joke-app .
    ```

2.  **Lancer le conteneur :**
    ```bash
    docker run --rm python-joke-app
    ```