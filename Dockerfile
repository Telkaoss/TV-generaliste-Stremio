# Utiliser une image Python officielle comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et l'installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application incluant le dossier app/
COPY . .

# Exposer le port sur lequel l'application s'exécute
EXPOSE 7000

# Commande pour exécuter l'application lorsque le conteneur démarre
CMD ["python", "main.py"] 