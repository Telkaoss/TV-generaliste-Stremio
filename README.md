# TV Generaliste pour Stremio

Un addon Stremio qui permet de regarder des chaînes TV françaises en direct.

## Fonctionnalités

- Accès aux chaînes TV françaises en streaming
- Interface simple et intuitive
- Mises à jour automatiques de la liste des chaînes
- Installation facile via le lien Stremio
- Entièrement configurable pour un déploiement personnalisé

## Installation

### Installation depuis Stremio

1. Accédez à votre installation de l'addon depuis votre navigateur
2. Cliquez sur le bouton d'installation 
3. Stremio s'ouvrira et vous proposera d'installer l'addon
4. Cliquez sur "Installer"

### Installation manuelle

Copiez l'URL du manifeste dans la section Addons de Stremio.

## Déploiement avec Docker

```bash
# Cloner le dépôt
git clone https://github.com/telkaoss/tv-generaliste-stremio.git
cd tv-generaliste-stremio

# Configuration
# 1. Créer un fichier .env ou configurer directement dans docker-compose.yml
# 2. Définir STREMIO_BASE_URL avec votre domaine public 
#    Exemple: STREMIO_BASE_URL=https://votre-domaine.com

# Lancer avec docker-compose
docker-compose up -d
```

### Configuration de l'URL de base (OBLIGATOIRE)

L'addon utilise une variable d'environnement `STREMIO_BASE_URL` pour configurer l'URL de base. **Cette configuration est obligatoire pour que l'addon fonctionne correctement.** 

Cette URL est utilisée pour:
- Les liens d'installation Stremio
- Les ressources statiques (images, icônes)
- Les liens dans le manifeste

Vous pouvez définir cette variable de plusieurs façons:

1. Dans le fichier `docker-compose.yml`:
   ```yaml
   environment:
     - STREMIO_BASE_URL=https://votre-domaine.com
   ```

2. Dans un fichier `.env` à la racine du projet:
   ```
   STREMIO_BASE_URL=https://votre-domaine.com
   ```

3. En la passant directement à Docker:
   ```bash
   docker run -e STREMIO_BASE_URL=https://votre-domaine.com -p 7000:7000 votre-image
   ```

Si la variable n'est pas correctement définie, les liens d'installation ne fonctionneront pas.

## Développement local

```bash
# Installer les dépendances
pip install -r requirements.txt

# Définir l'URL de base (pour Windows)
set STREMIO_BASE_URL=http://localhost:7000

# Définir l'URL de base (pour Linux/Mac)
export STREMIO_BASE_URL=http://localhost:7000

# Lancer l'application
python main.py
```

## License

MIT 