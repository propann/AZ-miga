# AZ-miga — inventaire de fichiers nécessaires

## ROM validées par Amiberry
Source : https://github.com/BlitterStudio/amiberry/wiki/Kickstart-ROMs-%28BIOS%29

Le fichier machine-lisible `data/kickstart-manifest.json` contient les **7 noms, modèles, versions et CRC32 exacts**. Les trois ROM A500 1.3, A600 2.05 et A1200 3.1 sont recommandées comme requises par le lanceur WHDLoad pour couvrir ses profils. Le nom du fichier peut différer : Amiberry identifie les ROM au checksum.

## Pour installer Workbench
- Disquettes originales d'installation AmigaOS/Workbench adaptées à Kickstart, généralement images ADF des médias : Install, Workbench, Extras, Fonts, Storage, Locale selon édition.
- Un disque dur virtuel HDF ou dossier hôte configuré dans Amiberry.
- Les fichiers système de l'installation AmigaOS doivent être installés à partir des médias autorisés ; les noms de disquettes changent selon version, édition et distribution. Il ne faut pas imposer une liste universelle trompeuse.
- Pour AmigaOS 3.2, utiliser le paquet d'installation et les ROM correspondantes légalement obtenues ; ne pas mélanger à l'aveugle Kickstart 3.1 et 3.2.

## WHDLoad et jeux
- Archives `.lha` de logiciels/jeux pour lesquels vous disposez des droits.
- Fichiers de boot WHDLoad d'Amiberry (whdboot), récupérables par le logiciel : https://github.com/BlitterStudio/amiberry/wiki/WHDLoad-Workflow
- Cas particulier de WHDLoad natif : fichiers de relocation Kickstart `.RTB` correspondants, disponibles par les canaux autorisés ; clé `rom.key` si requise par un format ROM chiffré. Voir https://www.whdload.de/docs/fr/need.html
- Autres médias pris en charge : ADF/ADZ/DMS/IPF, HDF/HDZ, ISO/CUE, selon le mode et les dépendances.

## Pour l'image Pi 4
- Raspberry Pi OS ARM64, kernel/pilotes BCM2711, pile DSI/DRM/KMS, libinput, environnement graphique, SDL3 et Amiberry.
- Pilote spécifique de dalle DSI et/ou tactile **seulement si le matériel ne fonctionne pas avec la prise en charge Linux existante**.
- Profil `.uae` A500 et A1200, création dans le logiciel après validation matérielle.
- Ne pas intégrer les fichiers propriétaires dans Git ni dans l'image publique.

## Vérification locale automatisée
```bash
python3 tools/check-kickstarts.py /chemin/vers/mes/roms
```
Sortie FOUND/MISSING/UNKNOWN. Compare le CRC32 réel, sans télécharger ou modifier les fichiers.
