import os
import time
from pathlib import Path
import subprocess
from datetime import datetime

# Chemins
archive_dir = Path.home() / "Desktop" / "Archivages"
log_file = Path.home() / "archivage.log"

# Durée de conservation (7 jours)
now = time.time()
seuil = 7 * 86400  # 7 jours en secondes

# Suppression des fichiers anciens
deleted_files = []
for file in archive_dir.glob("**/*"):
    if file.is_file() and now - file.stat().st_mtime > seuil:
        try:
            file.unlink()
            deleted_files.append(str(file))
        except Exception as e:
            print(f"Erreur lors de la suppression de {file} : {e}")

# Suppression des dossiers vides
for folder in sorted(archive_dir.glob("**/*"), reverse=True):
    if folder.is_dir() and not any(folder.iterdir()):
        try:
            folder.rmdir()
        except Exception as e:
            print(f"Erreur suppression dossier vide {folder} : {e}")

# Notification macOS
notif_cmd = [
    "osascript", "-e",
    'display notification "Le dossier Archivages a été nettoyé 🧹" with title "Nettoyage hebdo"'
]
subprocess.run(notif_cmd)

# Log
with open(log_file, "a") as f:
    f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Nettoyage : {len(deleted_files)} fichier(s) supprimé(s)\n")

