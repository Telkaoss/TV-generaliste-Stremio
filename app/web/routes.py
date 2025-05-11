import logging
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from app.config import TEMPLATES_DIR, ALL_CHANNELS, CATEGORIES, LAST_UPDATE, ADDON_ID, BASE_DIR, BASE_URL

# Initialiser le router
router = APIRouter()

# Initialiser les templates
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Page de dashboard avec bouton d'installation"""
    # Pour l'installation manuelle, garder l'URL HTTPS complète
    manifest_url = f"{BASE_URL}/manifest.json"
    # Utiliser l'hôte de la requête si disponible
    host = BASE_URL.replace("https://", "").replace("http://", "")
    if request and hasattr(request, 'headers') and 'host' in request.headers:
        host = request.headers.get('host')
        protocol = 'https' if request.url.scheme == 'https' else 'http'
        manifest_url = f"{protocol}://{host}/manifest.json"
    
    # ID pour le protocole stremio:///
    addon_id = ADDON_ID
    
    return templates.TemplateResponse(
        "dashboard.html", 
        {
            "request": request, 
            "channels_count": len(ALL_CHANNELS), 
            "category_count": len(CATEGORIES),
            "last_update": LAST_UPDATE,
            "manifest_url": manifest_url,
            "addon_id": addon_id,
            "host": host
        }
    ) 