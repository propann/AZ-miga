# AZ-miga 🪐

**Un Amiga moderne sur Raspberry Pi 4 avec écran DSI 10 pouces.**

> État : fondation documentaire et tests matériels à venir. Aucun démarrage réel sur le Raspberry Pi n'a encore été validé.

## Vision

AZ-miga transforme un Raspberry Pi 4 en ordinateur Amiga autonome : bureau Workbench, jeux ADF/WHDLoad, création graphique, trackers musicaux et trois profils matériels virtuels (A500, A1200 AGA et Amiga accéléré). L'écran DSI 10 pouces, le son, les périphériques USB et le démarrage en plein écran sont au cœur de l'expérience.

## Choix techniques initiaux

- Hôte : Raspberry Pi OS 64 bits (version compatible à confirmer sur le matériel).
- Émulateur principal : [Amiberry](https://github.com/BlitterStudio/amiberry), sans fork au départ.
- Profil par défaut : Amiga 1200 AGA avec Workbench.
- Profils additionnels : A500 orienté compatibilité et Amiga accéléré RTG/JIT sous réserve de benchmarks.
- Affichage : écran DSI **10 pouces**, modèle/résolution/tactile **non encore identifiés**. Ne pas appliquer d'overlay au hasard.
- Pilotage : clavier/souris et manette USB, SSH pour la maintenance.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Étude comparative et réutilisation de projets](docs/ETUDE-SOLUTIONS.md)
- [Écran DSI et validation matérielle](docs/HARDWARE-DSI.md)
- [Installation progressive](docs/INSTALLATION.md)
- [Feuille de route et critères de validation](docs/ROADMAP.md)
- [Cadre légal des ROM et contenus](docs/LEGAL.md)
- [Diagnostic matériel non destructif](scripts/diagnostic-pi4.sh)

## Démarrage rapide du travail

1. Relever le fabricant/modèle exact de l'écran 10 pouces et les caractéristiques du Pi 4.
2. Installer Raspberry Pi OS sur un support de test ; confirmer l'affichage DSI.
3. Lancer le diagnostic : `bash scripts/diagnostic-pi4.sh`.
4. Installer Amiberry conformément à `docs/INSTALLATION.md`.
5. Ajouter **localement** les ROM Kickstart et images système légalement obtenues.
6. Valider un A500, puis un A1200/Workbench, avant d'activer le lancement automatique.

## Philosophie

Réutiliser les projets libres plutôt que cloner leurs sources sans nécessité ; figer les versions et vérifier les licences avant toute intégration. Garder les données propriétaires, clés, jeux et disques virtuels personnels hors du dépôt.

## État de validation

Les documents et le script constituent une **base de projet**. Aucun test physique n'a été réalisé sur le Pi 4 ou l'écran DSI 10 pouces à ce stade.
