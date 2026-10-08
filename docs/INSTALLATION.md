# Installation progressive — Pi 4 (non encore testée sur le matériel)

## 0. Sécurité

Utiliser une microSD de test et conserver une sauvegarde. Ne pas lancer de script tiers sans le lire ; ne pas modifier d'overlay DSI sans référence écran.

## 1. Préparer Raspberry Pi OS

Installer Raspberry Pi OS 64 bits avec bureau via Raspberry Pi Imager ; SSH facultatif. Après le premier démarrage :

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

Après redémarrage :

```bash
uname -m
bash scripts/diagnostic-pi4.sh
```

La sortie doit indiquer `aarch64` pour ARM64. Valider DSI et audio avant l'émulation.

## 2. Installer Amiberry depuis son dépôt officiel

Documentation : https://github.com/BlitterStudio/amiberry/wiki/Quick-start-guide

```bash
curl -fsSL https://packages.amiberry.com/install.sh -o /tmp/amiberry-install.sh
less /tmp/amiberry-install.sh
# seulement après examen du script :
sudo sh /tmp/amiberry-install.sh
sudo apt update
sudo apt install amiberry
```

Puis lancer `amiberry` depuis une session graphique. Le paquet/système exact sera vérifié lors du test physique.

## 3. Premier boot Amiga

Ouvrir Quickstart, choisir A500, associer une ROM Kickstart obtenue légalement et un média de test autorisé, puis démarrer. Sauvegarder une configuration stable avant toute optimisation.

## 4. A1200 / Workbench

Charger Kickstart compatible, créer un disque dur virtuel, installer Workbench depuis ses médias légitimes. Tester le bureau, la souris, le clavier, l'audio et la persistance.

## 5. Profil accéléré

N'activer JIT/RTG qu'après benchmark, et ne pas confondre compatibilité A500/AGA avec performance du profil accéléré.

## 6. Boot direct

Non implémenté à cette étape. Prévoir un mode de récupération qui laisse le système Linux accessible si le launcher ou le DSI échoue.
