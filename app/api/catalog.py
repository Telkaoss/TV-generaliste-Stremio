import logging
import re
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.config import ID_PREFIX, CATEGORIES

router = APIRouter()

@router.get("/catalog/tv/tv-{category_id}.json")
async def get_catalog(category_id: str):
    """Retourne le catalogue pour une catégorie spécifique"""
    logging.debug(f"Requête reçue pour le catalogue TV de la catégorie: {category_id}")
    
    # Trouver la catégorie correspondante
    for category in CATEGORIES.keys():
        cat_id = re.sub(r'[^a-zA-Z0-9]', '', category.lower())
        if cat_id == category_id:
            channels = CATEGORIES[category]
            metas = []
            
            for channel in channels:
                metas.append({
                    "id": f"{ID_PREFIX}:{channel['id']}",
                    "type": "tv",
                    "name": channel['name'],
                    "poster": channel['icon'],
                    "description": f"Regarder {channel['name']} en direct (Catégorie: {category})."
                })
            
            logging.debug(f"Catalogue TV généré pour la catégorie {category} avec {len(metas)} éléments")
            return JSONResponse(content={"metas": metas})
    
    # Si la catégorie n'est pas trouvée
    logging.error(f"Catégorie non trouvée: {category_id}")
    raise HTTPException(status_code=404, detail="Category not found") 