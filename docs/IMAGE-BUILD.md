# Image AZ-miga : constructeur expérimental

**Statut : code publié, image non encore construite ni validée sur le matériel.**

Le constructeur exploite [pi-gen](https://github.com/RPi-Distro/pi-gen), Raspberry Pi OS Trixie ARM64 et le paquet [Amiberry](https://packages.amiberry.com/). Il ajoute l'ouverture automatique de l'interface Amiberry dans le bureau, mais pas encore un Workbench installé.

## Fabrication

Sur une machine Linux x86_64 avec Docker, permissions de conteneurs privilégiés et plusieurs dizaines de Go disponibles :

```bash
git clone https://github.com/propann/AZ-miga.git
cd AZ-miga
bash scripts/build-image.sh
```

L'archive produite, si le build aboutit, est dans `.build/pi-gen/deploy/`. Décompresser le ZIP pour obtenir le fichier `.img` puis flasher avec Raspberry Pi Imager.

Sur GitHub : **Actions → Build experimental AZ-miga image → Run workflow**. En cas de succès, télécharger l'artifact ZIP (rétention 7 jours). Les limites de stockage des runners GitHub peuvent faire échouer une construction lourde.

## Installation et premiers tests

- Première configuration de Raspberry Pi OS (compte utilisateur sans mot de passe prédéfini).
- DSI 10 pouces : identifier le modèle exact pour configurer le pilote ; aucun overlay aléatoire n'est imposé.
- Amiberry démarre à l'ouverture de session. Ajouter les ROM Kickstart et médias Workbench obtenus légalement.
- Profils A500 puis A1200 : les configurer et tester sur matériel réel.
- Retour bureau : `sudo mv /etc/xdg/autostart/az-miga.desktop /etc/xdg/autostart/az-miga.desktop.disabled`.

## Avant une version stable

Valider un build réussi, contrôle SHA256, boot physique du Pi4, DSI, son, clavier, souris, un A500, un A1200 Workbench et la récupération du bureau. Pinner les versions pi-gen/Amiberry pour la reproductibilité. Aucune image n'est encore annoncée comme prête.

Sources : https://github.com/RPi-Distro/pi-gen ; https://github.com/BlitterStudio/amiberry/wiki/Quick-start-guide
