import logging
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import re
from app.config import ADDON_ID, ID_PREFIX, CATEGORIES, CATEGORY_ORDER, BASE_URL

router = APIRouter()

@router.get("/manifest.json")
async def get_manifest(request: Request = None):
    """Retourne le manifest pour Stremio"""
    logging.debug("Requête reçue pour /manifest.json")
    
    # Obtenir l'URL de base pour les ressources
    base_url = BASE_URL
    if request:
        # Si la requête contient un hôte, utiliser celui-ci en priorité
        host = request.headers.get("host", "")
        if host:
            protocol = "https" if request.url.scheme == "https" else "http"
            base_url = f"{protocol}://{host}"
    
    # Créer un catalogue pour chaque catégorie
    catalogs = []
    for category in CATEGORY_ORDER:
        # Créer un ID de catalogue valide (en supprimant les caractères non alphanumériques)
        catalog_id = re.sub(r'[^a-zA-Z0-9]', '', category.lower())
        if not catalog_id:
            catalog_id = "autres"
        
        catalogs.append({
            "type": "tv",
            "id": f"tv-{catalog_id}",
            "name": category
        })
    
    manifest = {
        "id": ADDON_ID,
        "version": "0.2.0",
        "name": "TV Generaliste",
        "description": "Chaînes TV généralistes en direct organisées par catégories.",
        "logo": f"{base_url}/static/tv_icon.svg",
        "background": f"{base_url}/static/tv_background.svg",
        "resources": [
            {
                "name": "catalog",
                "types": ["tv"],
                "idPrefixes": [ID_PREFIX]
            },
            {
                "name": "stream",
                "types": ["tv"],
                "idPrefixes": [ID_PREFIX]
            },
            {
                "name": "meta",
                "types": ["tv"],
                "idPrefixes": [ID_PREFIX]
            }
        ],
        "types": ["tv"],
        "catalogs": catalogs,
        "idPrefixes": [ID_PREFIX]
    }
    logging.debug(f"Manifest généré : {manifest}")
    return JSONResponse(content=manifest) 