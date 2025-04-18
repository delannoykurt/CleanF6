# 🔁 Script de Nettoyage Hebdomadaire – Archivages

Ce projet contient un script Python conçu pour nettoyer automatiquement le dossier `~/Desktop/Archivages` en supprimant les fichiers vieux de plus de 7 jours, tout en générant une notification macOS et un fichier de log.

> 💡 Ce script est déclenché via la touche **F6**, remappée à l’aide de [Karabiner-Elements](https://karabiner-elements.pqrs.org) sur un clavier secondaire non Apple.

---

## 🎯 Objectif

- Garder un bureau propre et fonctionnel
- Supprimer les fichiers obsolètes automatiquement
- Lancer le tout d’un seul geste (F6)
- Préserver une trace dans un fichier de log

---

## 📦 Contenu

- `nettoyage_archivages.py` → Le script principal
- `archivage.log` → Log des opérations (créé automatiquement)
- `README.md` → Ce fichier

---

## 🧰 Prérequis

- macOS
- Python 3 installé
- [Karabiner-Elements](https://karabiner-elements.pqrs.org) pour le mapping clavier

---

## ⚙️ Installation

1. Clone ou copie ce dépôt dans ton dossier personnel :
   ```bash
   mkdir -p ~/scripts && cd ~/scripts
   # Ajoute ici ton script Python

