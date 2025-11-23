# Utiliser une image Python légère comme base
FROM python:3.9-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code (app.py, README, etc.)
COPY . .

# Commande à exécuter au démarrage du conteneur
CMD ["python", "app.py"]