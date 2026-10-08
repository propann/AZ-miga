# AZ-miga : Workbench d'abord

## Produit cible
Le Raspberry Pi 4 démarre dans un **Workbench Amiga natif** (via Amiberry), personnalisé pour DSI tactile 10 pouces. La bibliothèque est accessible *depuis ce bureau*, et non depuis un frontend Linux qui remplace Workbench.

## Deux façons de lancer des jeux depuis Workbench
**A — WHDLoad dans le Workbench en cours (préférée).** Installer légalement les jeux sur le disque Amiga, WHDLoad et ses dépendances. Ouvrir leurs icônes depuis Workbench. Un jeu prend le contrôle de la machine pendant son exécution puis un raccourci QuitKey permet de revenir au Workbench, lorsque l'install le prend en charge. Cette solution est idéale pour un bureau persistant, mais pas universelle.

**B — Disquettes ADF / jeux non compatibles WHDLoad.** Lancer une *configuration Amiberry adaptée au titre* ; certains jeux doivent booter seuls en A500 Kickstart 1.3 OCS/ECS, d'autres en A1200 AGA. Il n'est pas possible de promettre que chaque ADF boote dans un A1200 modernisé déjà actif sans redémarrage de l'Amiga virtuel. Le frontend tactile devra indiquer le changement de profil et proposer un retour clair au Workbench.

Ne pas confondre le booter WHDLoad d'Amiberry (auto-charge une archive LHA et configure une session de jeu distincte) avec le lancement d'un slave WHDLoad *dans* le Workbench déjà démarré. Les deux chemins seront supportés.

## Implantation par étapes
1. Raspberry Pi OS et DSI fonctionnels ; Amiberry et ROM autorisées.
2. Profil A1200 Workbench 3.x et disque dur persistant ; raccourci retour.
3. Installer WHDLoad dans l'Amiga, créer un premier raccourci jeu lancé depuis Workbench.
4. Ajouter volumes Jeux / Musique / Outils et icônes adaptées ; personnalisation Workbench sans remplacer les composants système.
5. Ajouter sélection A500/A1200 séparée pour titres incompatibles, avec gestion d'arrêt et redémarrage de l'émulation.
6. Surcouche tactile : clavier à l'écran, bouton souris droit, raccourcis, QuitKey ; tester sous Linux puis Workbench.
7. Seulement après validation, configurer un lancement automatique du profil Workbench, pas juste l'interface Amiberry.

## Organisation des contenus personnels (hors dépôt public)
- HD Workbench installé (HDF ou répertoire hôte dédié).
- SYS: pour le système, WORK: pour les applications.
- GAMES: pour installations WHDLoad; DISKS: pour ADF et images de jeux.
- Exports sauvegardés indépendamment de l'image SD.
- Ne jamais publier Kickstart, Workbench ou jeux propriétaires.

## Compatibilité attendue
- A500 OCS/ECS : émulation séparée fiable avec Kickstart 1.3 pour les logiciels stricts.
- A1200 AGA : Workbench quotidien et jeux AGA.
- WHDLoad : accélérateur de confort pour jeux installés, compatibilité à tester titre par titre.
- Tactile : fonctionne comme pointeur souris si pris en charge ; clavier virtuel et clic droit à développer.

## Références
- https://www.whdload.de/docs/fr/opt.html
- https://github.com/BlitterStudio/amiberry/wiki/WHDLoad-Workflow
- https://github.com/BlitterStudio/amiberry/wiki/WHDLoad-Auto-booting
