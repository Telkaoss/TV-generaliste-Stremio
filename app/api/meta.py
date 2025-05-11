import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.config import ID_PREFIX, ALL_CHANNELS

router = APIRouter()

@router.get("/meta/tv/{stremio_id}.json")
async def get_meta_item(stremio_id: str):
    """Retourne les métadonnées d'une chaîne spécifique"""
    logging.debug(f"Requête reçue pour les méta-données de TV: {stremio_id}")

    if not stremio_id.startswith(ID_PREFIX + ":"):
        logging.error(f"ID de méta invalide (préfixe attendu '{ID_PREFIX}:') : {stremio_id}")
        raise HTTPException(status_code=404, detail="Invalid meta ID prefix")

    channel_id = stremio_id.split(":")[-1]
    
    # Rechercher dans toutes les chaînes
    channel_data = ALL_CHANNELS.get(channel_id)
    
    if not channel_data:
        logging.error(f"Chaîne non trouvée (pour méta) pour l'ID: {channel_id}")
        raise HTTPException(status_code=404, detail="Channel not found for meta")

    meta_object = {
        "id": stremio_id,
        "type": "tv",
        "name": channel_data["name"],
        "poster": channel_data["icon"],
        "background": channel_data["icon"],
        "posterShape": "square",
        "logo": channel_data["icon"],
        "description": f"Regarder {channel_data['name']} en direct (Catégorie: {channel_data['group']})."
    }
    logging.debug(f"Méta-données TV générées pour {stremio_id}: {meta_object}")
    return JSONResponse(content={"meta": meta_object}) 