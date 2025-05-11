import os
from app.config import STATIC_DIR, TEMPLATES_DIR

# Définition du HTML pour le dashboard
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TV Generaliste - Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #121212;
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        .container {
            text-align: center;
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            max-width: 500px;
            width: 90%;
        }
        .logo {
            width: 100px;
            height: 100px;
            margin-bottom: 20px;
            border-radius: 50%;
            background-color: #e50914;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px auto;
        }
        .logo img {
            width: 70px;
            height: 70px;
            filter: brightness(0) invert(1);
        }
        h1 {
            margin-top: 0;
            color: #e50914;
            font-size: 24px;
        }
        p {
            color: #aaa;
            margin-bottom: 30px;
            font-size: 16px;
            line-height: 1.5;
        }
        .install-btn {
            background-color: #e50914;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            transition: background-color 0.3s;
        }
        .install-btn:hover {
            background-color: #f40612;
        }
        .stats {
            margin-top: 30px;
            display: flex;
            justify-content: space-around;
            background-color: #252525;
            border-radius: 10px;
            padding: 15px;
        }
        .stat-item {
            text-align: center;
        }
        .stat-item .value {
            font-size: 24px;
            font-weight: bold;
            color: #e50914;
        }
        .stat-item .label {
            font-size: 14px;
            color: #aaa;
        }
        footer {
            margin-top: 40px;
            color: #666;
            font-size: 12px;
        }
        .manual-install {
            margin-top: 20px;
            background-color: #252525;
            border-radius: 5px;
            padding: 15px;
        }
        .manual-install h3 {
            color: #aaa;
            font-size: 16px;
            margin-top: 0;
            margin-bottom: 10px;
        }
        .url-box {
            background-color: #333;
            padding: 10px;
            border-radius: 5px;
            word-break: break-all;
            font-family: monospace;
            font-size: 14px;
            margin-bottom: 10px;
            color: #0f0;
        }
        .copy-btn {
            background-color: #333;
            color: #fff;
            border: 1px solid #555;
            padding: 8px 15px;
            font-size: 14px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .copy-btn:hover {
            background-color: #444;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="/static/tv_icon.svg" alt="TV Generaliste Logo">
        </div>
        <h1>TV Generaliste</h1>
        <p>Addon Stremio pour regarder les chaînes TV en direct. Organisé en une catégorie globale pour un accès facile à toutes les chaînes.</p>
        
        <a href="stremio://{{ host }}/manifest.json" class="install-btn">Installer l'addon</a>
        
        <div class="manual-install">
            <h3>Installation manuelle</h3>
            <div class="url-box" id="manifest-url">{{ manifest_url }}</div>
            <button class="copy-btn" onclick="copyToClipboard()">Copier l'URL</button>
        </div>
        
        <div class="stats">
            <div class="stat-item">
                <div class="value">{{ channels_count }}</div>
                <div class="label">Chaînes disponibles</div>
            </div>
            <div class="stat-item">
                <div class="value">{{ category_count }}</div>
                <div class="label">Catégorie</div>
            </div>
        </div>
    </div>
    <footer>
        Version: 0.2.0 &bull; Dernière mise à jour: {{ last_update }}
    </footer>
    
    <script>
    function copyToClipboard() {
        var copyText = document.getElementById("manifest-url");
        navigator.clipboard.writeText(copyText.textContent)
            .then(() => {
                alert("URL du manifest copiée !");
            })
            .catch(err => {
                console.error('Erreur lors de la copie :', err);
            });
    }
    </script>
</body>
</html>
"""

# Définition de l'icône SVG
TV_ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#e50914" stroke="#ffffff" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="7" width="20" height="15" rx="2" ry="2" fill="#202020" stroke="#e50914" stroke-width="1.5" />
  <polyline points="17 2 12 7 7 2" stroke="#e50914" stroke-width="1.5" />
  <circle cx="8" cy="13" r="1" fill="#ffffff" />
  <circle cx="12" cy="13" r="1" fill="#ffffff" />
  <circle cx="16" cy="13" r="1" fill="#ffffff" />
  <line x1="8" y1="17" x2="16" y2="17" stroke="#ffffff" stroke-width="1.5" />
</svg>"""

# Définition du fond d'écran en SVG
TV_BACKGROUND_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#000000;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e50914;stop-opacity:0.7" />
    </linearGradient>
  </defs>
  <rect width="1280" height="720" fill="url(#grad1)" />
  <g transform="translate(640, 360) scale(15)" fill="#ffffff" opacity="0.1">
    <rect x="2" y="7" width="20" height="15" rx="2" ry="2" />
    <polyline points="17 2 12 7 7 2" />
    <circle cx="8" cy="13" r="1" />
    <circle cx="12" cy="13" r="1" />
    <circle cx="16" cy="13" r="1" />
    <line x1="8" y1="17" x2="16" y2="17" stroke="#ffffff" stroke-width="1.5" />
  </g>
</svg>"""

def save_static_files():
    """
    Crée les fichiers statiques et templates nécessaires s'ils n'existent pas.
    """
    # Créer le template HTML
    template_path = os.path.join(TEMPLATES_DIR, "dashboard.html")
    if not os.path.exists(template_path):
        with open(template_path, "w", encoding="utf-8") as f:
            f.write(DASHBOARD_HTML)
    
    # Créer l'icône SVG
    icon_path = os.path.join(STATIC_DIR, "tv_icon.svg")
    if not os.path.exists(icon_path):
        with open(icon_path, "w", encoding="utf-8") as f:
            f.write(TV_ICON_SVG)
            
    # Créer l'image de fond SVG
    background_path = os.path.join(STATIC_DIR, "tv_background.svg")
    if not os.path.exists(background_path):
        with open(background_path, "w", encoding="utf-8") as f:
            f.write(TV_BACKGROUND_SVG) 