# AZ-miga — dalle DSI 10 pouces et tactile

## Matériel encore inconnu
Taille 10 pouces et fonction tactile confirmées. Marque, contrôleur DSI, pilote, contrôleur tactile, résolution et alimentation inconnus. Ne **jamais** choisir un overlay au hasard.

## Étages matériels
1. DSI du Pi4 -> noyau DRM/KMS + pilote panneau + rétroéclairage.
2. Contrôleur tactile distinct (I2C, USB, SPI selon modèle) -> pilote noyau/input evdev.
3. libinput -> orientation et matrice de calibration ; assignation au bon écran.
4. labwc/Wayland : mapping du tactile à l'écran DSI et émulation souris si nécessaire. Documentation : https://github.com/raspberrypi-ui/labwc-latest/blob/master/docs/labwc-config.5.scd
5. SDL3 / Amiberry : activer dans GUI/Input « Install virtual mouse driver », « Tablet mode », puis comparer MouseHack/Real Tablet. Documentation https://github.com/BlitterStudio/amiberry/wiki/GUI-Input

## Procédure de validation
1. Démarrer Pi OS et obtenir une image DSI native.
2. `sh scripts/diagnostic-touch.sh` ; conserver les résultats et version du système.
3. Tester le tactile sur le bureau : 4 coins, centre, appui long, glissement, bordures.
4. En cas de rotation/échelle erronée, utiliser configuration libinput / labwc spécifique au périphérique. Sauvegarder le fichier de configuration avant changement ; ne pas appliquer de règles globales qui affecteraient un second écran.
5. Démarrer Amiberry et valider les interactions souris absolues dans Workbench ; garder clavier/souris USB pour configuration/récupération.
6. Tester passage plein écran, redimensionnement, changement de profil et réouverture.

## Développement pilote : seulement après identification du matériel
- Si le tactile apparaît dans `/proc/bus/input/devices` et fonctionne en bureau, un pilote maison serait contre-productif.
- Sinon identifier USB VID/PID ou I2C, noyau, log dmesg, datasheet et driver officiel.
- Privilégier driver mainline/dtoverlay upstream ; n'écrire un module ou overlay spécifique qu'après preuve d'absence de support.
- Un clavier virtuel et une barre de commandes tactiles AZ-miga seront une **surcouche d'interface**, pas un pilote noyau.
- Aucun pilote ni calibrage écran n'a encore été testé physiquement.
