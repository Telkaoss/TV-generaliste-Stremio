import logging
import uvicorn
from app import create_app

# Créer l'application avec la nouvelle structure modulaire
app = create_app()

# Point d'entrée pour exécuter l'application avec Uvicorn
if __name__ == "__main__":
    port = 7000  # Vous pouvez changer le port si nécessaire
    logging.info(f"Démarrage du serveur de l'addon Stremio TV Française sur http://127.0.0.1:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port) 