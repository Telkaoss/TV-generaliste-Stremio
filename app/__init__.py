import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router
from app.web import router as web_router, setup_static_files
from app.parser import download_and_parse_m3u, start_update_thread
from app.web.utils import save_static_files

def create_app():
    """Crée et configure l'application FastAPI"""
    # Créer l'application
    app = FastAPI()
    
    # Autoriser CORS pour que Stremio puisse accéder à l'addon localement
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # Ou spécifiez l'origine de Stremio si connue et fixe
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Configurer les fichiers statiques
    setup_static_files(app)
    
    # S'assurer que les fichiers statiques nécessaires existent
    save_static_files()
    
    # Inclure les routers
    app.include_router(api_router)
    app.include_router(web_router)
    
    # Télécharger la liste M3U au démarrage
    if not download_and_parse_m3u():
        # Si le téléchargement échoue, nous aurons un catalogue vide mais l'application démarrera quand même
        logging.warning("Impossible de télécharger la liste M3U initiale. Le catalogue sera vide.")
    
    # Démarrer la mise à jour périodique
    start_update_thread()
    
    return app 