import logging
import requests
import re
import time
import threading
from datetime import datetime
from app.config import CATEGORIES, ALL_CHANNELS, CATEGORY_ORDER, LAST_UPDATE, M3U_URL

def download_and_parse_m3u():
    """
    Télécharge et parse la liste M3U pour extraire les chaînes TV.
    Organise toutes les chaînes dans une seule catégorie "Chaines Global".
    """
    global LAST_UPDATE
    try:
        logging.info(f"Téléchargement de la liste M3U depuis {M3U_URL}")
        response = requests.get(M3U_URL, timeout=20)
        response.raise_for_status()
        
        content = response.text
        
        # Nettoyage des catégories et des chaînes
        CATEGORIES.clear()
        ALL_CHANNELS.clear()
        CATEGORY_ORDER.clear()
        
        # Créer la catégorie "Chaines Global"
        CATEGORIES["Chaines Global"] = []
        CATEGORY_ORDER.append("Chaines Global")
        
        # Parser le contenu M3U
        lines = content.strip().split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Ignorer les lignes vides ou l'en-tête M3U
            if not line or line == "#EXTM3U":
                i += 1
                continue
            
            # Chercher les lignes d'info des chaînes
            if line.startswith("#EXTINF:"):
                # Extraire les métadonnées de la chaîne
                channel_info = line
                
                # Extraire le logo
                logo_match = re.search(r'tvg-logo="([^"]+)"', channel_info)
                logo = logo_match.group(1) if logo_match else ""
                
                # Extraire le nom de la chaîne (tout ce qui suit après la dernière virgule)
                name_match = re.search(r',([^,]+)$', channel_info)
                name = name_match.group(1).strip() if name_match else f"Channel {i}"
                
                # La ligne suivante devrait contenir l'URL de la chaîne
                i += 1
                if i < len(lines):
                    url = lines[i].strip()
                    
                    # Ignorer les entrées sans URL valide ou contenant 'frembed'
                    if not url or url.startswith('#') or url == "http://" or "frembed" in url.lower():
                        i += 1
                        continue
                    
                    # Créer un ID basé sur le nom (en remplaçant les caractères non alphanumériques)
                    channel_id = re.sub(r'[^a-zA-Z0-9]', '', name.lower())
                    if not channel_id:  # Fallback si l'ID est vide
                        channel_id = f"channel_{i}"
                    
                    # Stocker les informations de la chaîne dans la catégorie "Chaines Global" seulement
                    channel_data = {
                        "id": channel_id,
                        "name": name,
                        "icon": logo,
                        "group": "Chaines Global",
                        "url": url
                    }
                    
                    # Ajouter toutes les chaînes à la catégorie "Chaines Global"
                    CATEGORIES["Chaines Global"].append(channel_data)
                    ALL_CHANNELS[channel_id] = channel_data
            
            i += 1
        
        # Mettre à jour la date et l'heure de la dernière mise à jour
        global LAST_UPDATE
        LAST_UPDATE = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        logging.info(f"Liste M3U parsée avec succès : {len(ALL_CHANNELS)} chaînes dans la catégorie Chaines Global")
        return True
    except Exception as e:
        logging.error(f"Erreur lors du téléchargement ou du parsing de la liste M3U : {str(e)}")
        return False

def update_m3u_periodically(interval_hours=12):
    """Lance la mise à jour périodique de la liste M3U"""
    while True:
        time.sleep(interval_hours * 3600)  # Conversion en secondes
        logging.info(f"Mise à jour programmée de la liste M3U (toutes les {interval_hours}h)")
        download_and_parse_m3u()

def start_update_thread(interval_hours=12):
    """Démarre le thread de mise à jour périodique"""
    thread = threading.Thread(
        target=update_m3u_periodically, 
        args=(interval_hours,), 
        daemon=True
    )
    thread.start()
    return thread 