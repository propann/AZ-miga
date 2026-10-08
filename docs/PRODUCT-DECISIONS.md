# AZ-miga — décision produit (2026-10-08)

## Objectif unique
Faire démarrer un **vrai Workbench Amiga classique modernisé** sur Raspberry Pi 4 et écran DSI tactile 10 pouces, avec lancement fiable des jeux et applications **Amiga 500 et Amiga 1200**.

## Architecture
- Raspberry Pi OS ARM64 + Amiberry.
- Environnement principal : A1200 AGA / Workbench 3.x, disque virtuel persistant. Évaluer AmigaOS 3.2 si licence disponible, sans supposer que 3.2 est indispensable.
- Jeu A500 : profil Kickstart 1.3 + OCS/ECS + réglages de vitesse/timing dédiés.
- Jeu A1200 : profil Kickstart 3.1 + AGA ; WHDLoad si l'installation et ses droits sont disponibles.
- Lanceur de jeux qui bascule le profil d'émulation : jamais supposer que toutes les productions A500 marchent sur le Workbench A1200 accéléré.
- Tactile : libinput/SDL, souris absolue si opérationnelle ; clavier logiciel et contrôles de secours à développer.
- Interface : Workbench natif avec extensions d'icônes, thèmes, utilitaires, gestionnaire de fichiers ; évaluer MUI, MagicWB, outils actuels selon licences, stabilité et performances.

## AROS : non retenu pour produit principal
AROS peut servir de ROM de dépannage ou de banc de test séparé, mais pas d'OS à installer à la place de Workbench. Ne pas faire de l'édition AROS un jalon bloquant ni l'inclure comme mode principal dans l'image distribuée.

## Fichiers à obtenir légalement
- Kickstart 1.3 A500 (ROM).
- Kickstart 3.1 A1200 (ROM).
- Kickstart 2.05 A600 : conseillé pour certains titres WHDLoad.
- Images d'installation AmigaOS/Workbench 3.x dont on détient la licence.
- Installateur WHDLoad et composants requis si choisi.
- Jeux ADF/LHA/HDF acquis légalement, à ajouter par l'utilisateur.
- Aucune ROM commerciale, disquette système ou jeu embarqués dans Git ou une image publique.

## Validation
1. Boot Pi 4 + écran DSI, tactile et audio.
2. Amiberry et Workbench 3.x installé depuis médias légitimes.
3. Iconographie moderne, bureau utilisable et stable.
4. Jeu A500 lancé et retour au bureau.
5. Jeu A1200 AGA lancé et retour au bureau.
6. Paramètres, profils, sauvegardes et mapping tactile persistants.
7. Image reproductible, prête à personnaliser avec ses ROM légales.
