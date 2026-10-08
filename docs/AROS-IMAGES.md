# AZ-miga — étude et inventaire des images AROS

Date : 2026-10-08. Statut : références documentées, **aucun démarrage testé sur Pi4**.

## Pourquoi AROS ?
AROS est une réimplémentation libre de l'environnement Amiga. Pour Amiberry, choisir les images **amiga-m68k** (68k) : les builds linux-arm sont des environnements hébergés ARM et ne constituent PAS une ROM Amiga pour l'émulateur.

## Fichiers à collecter

| Composant | Rôle | Nécessaire au premier test |
|---|---|---|
| `AROS-<date>-amiga-m68k-boot-floppy.zip` | Disquette de boot 68k à extraire | Oui, test initial |
| `AROS-<date>-amiga-m68k-boot-iso.zip` | CD-ROM AROS 68k et fichiers cœur | Oui, installation/étude |
| `AROS-<date>-amiga-m68k-contrib.*` | Paquets et applications complémentaires | Non |
| `aros-rom.bin` | Image ROM principale AROS 68k | Oui, selon émulateur/montage |
| `aros-ext.bin` | ROM étendue AROS 68k | Selon variante/émulateur |
| `amiga-m68k-classic` | Build classique plus léger, sans composants superflus | Test complémentaire |

Les noms exacts des archives et l'emplacement des ROM varient selon date et édition du build : inspecter le ZIP/ISO, ne pas inventer de chemin stable. Documenter la source, la date, l'empreinte SHA256 et la licence des fichiers que nous déciderons d'intégrer.

## Sources officielles
- https://www.aros.org/download.html
- https://www.aros.org/cgi-bin/files?lang=en&type=nightly2
- https://sourceforge.net/projects/aros/files/nightly2/
- Code : https://github.com/aros-development-team/AROS
- Instructions des variantes 68k : https://github.com/deadwood2/AROS/blob/master/INSTALL.md

## Architecture prévue
1. Mode Classic : ROM Kickstart licenciée + Workbench licencié + WHDLoad.
2. Mode AROS 68k : ROM AROS + environnement AROS installé sur un disque virtuel dédié.
3. AROS host ARM (option expérimentale séparée) : système hosted Linux/ARM, sans Amiberry ; **ne pas confondre** avec AROS 68k.

## Limites
La ROM AROS incluse comme secours dans Amiberry ne remplace pas toutes les ROM Kickstart commerciales pour les jeux et le lanceur automatique WHDLoad. Les nightly AROS ne sont pas validées comme un environnement stable. Les licences des binaires, applications et ressources de chaque distribution doivent être examinées avant republication.

## Plan de validation
- [ ] Télécharger les images 68k depuis les sources officielles, vérifier date et SHA256.
- [ ] Examiner les fichiers à l'intérieur des archives et la licence.
- [ ] Charger la ROM AROS sur le profil Amiberry dédié.
- [ ] Démarrer l'ADF de boot ou l'ISO sur le Pi4.
- [ ] Installer sur HDF et tester Wanderer, clavier, souris et audio.
- [ ] Valider écran DSI 10 pouces et correspondance tactile/souris.
- [ ] Comparer avec le profil Workbench classique sans écraser ses paramètres.
