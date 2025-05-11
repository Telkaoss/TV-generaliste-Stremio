from fastapi import APIRouter
from app.api import manifest, catalog, meta, stream

# Créer un router API principal
router = APIRouter()

# Inclure tous les routers des sous-modules
router.include_router(manifest.router)
router.include_router(catalog.router)
router.include_router(meta.router)
router.include_router(stream.router) 