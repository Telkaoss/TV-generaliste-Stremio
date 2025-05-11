from fastapi import APIRouter
from app.web.routes import router as web_router
from fastapi.staticfiles import StaticFiles
from app.config import STATIC_DIR

# Créer un router web principal
router = APIRouter()

# Inclure le router des routes web
router.include_router(web_router)

# Fonction pour configurer les fichiers statiques
def setup_static_files(app):
    """Configure les fichiers statiques pour l'application"""
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static") 