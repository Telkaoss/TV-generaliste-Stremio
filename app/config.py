import logging
import os
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# URL de base pour l'addon (doit être configurée par l'utilisateur via variable d'environnement)
BASE_URL = os.environ.get("STREMIO_BASE_URL", "http://localhost:7000")

# Variables globales
ADDON_ID = "org.generaliste.tv.python"
ID_PREFIX = "gtv"  # Préfixe pour les ID des chaînes dans Stremio

# URL de la liste M3U
M3U_URL = "https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/all.m3u"

# Dictionnaire pour stocker les chaînes, organisées par catégorie
CATEGORIES = {}
# Dictionnaire pour stocker les détails de toutes les chaînes
ALL_CHANNELS = {}
# Liste pour stocker les noms des catégories dans l'ordre
CATEGORY_ORDER = []
# Dernière mise à jour
LAST_UPDATE = "Jamais"

# Chemins des ressources
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "app" / "web" / "static"
TEMPLATES_DIR = BASE_DIR / "app" / "web" / "templates"

# Assurer que les répertoires existent
STATIC_DIR.mkdir(exist_ok=True, parents=True)
TEMPLATES_DIR.mkdir(exist_ok=True, parents=True) 