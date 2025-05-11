import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.config import ID_PREFIX, ALL_CHANNELS

router = APIRouter()

@router.get("/stream/tv/{stremio_id}.json")
async def get_stream(stremio_id: str):
    """Retourne les streams disponibles pour une chaîne spécifique"""
    logging.debug(f"Requête reçue pour le flux TV de {stremio_id}")
    
    if not stremio_id.startswith(ID_PREFIX + ":"):
        logging.error(f"ID de flux invalide (préfixe attendu '{ID_PREFIX}:') : {stremio_id}")
        raise HTTPException(status_code=404, detail="Invalid stream ID prefix")

    channel_id = stremio_id.split(":")[-1]
    
    # Rechercher dans toutes les chaînes
    channel_data = ALL_CHANNELS.get(channel_id)
            
    if not channel_data:
        logging.error(f"Chaîne non trouvée pour l'ID: {channel_id}")
        raise HTTPException(status_code=404, detail="Channel not found")

    # Utiliser l'URL directe de la chaîne
    stream_url = channel_data['url']
    
    # Vérifier si l'URL se termine par .m3u8 ou .ts (flux HLS standard)
    if stream_url.endswith('.m3u8') or stream_url.endswith('.ts'):
        streams = [{
            "name": f"{channel_data['name']} - Direct",
            "url": stream_url,
            "title": f"{channel_data['name']} - Direct"
        }]
    else:
        # Pour les autres types d'URL, utiliser externalUrl pour ouvrir dans un navigateur
        streams = [{
            "name": f"{channel_data['name']} - Externe",
            "externalUrl": stream_url,
            "title": f"{channel_data['name']} - Externe"
        }]
    
    logging.debug(f"Flux TV généré pour {channel_data['name']} ({stremio_id}): {streams}")
    return JSONResponse(content={"streams": streams}) 