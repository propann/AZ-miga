# AZ-miga ROM Center — étude et spécification

## Philosophie
Reconnaissance locale des fichiers que l'utilisateur possède, puis enrichissement via des **métadonnées publiques autorisées**. Jamais de téléchargement automatique de ROM commerciales, de partage des contenus, d'upload d'empreintes personnelles sans consentement ou de contournement de protections.

## Catalogue requis

| Groupe | Fichiers / formats | Statut |
|---|---|---|
| Base Linux | Raspberry Pi OS ARM64 et Amiberry | Installés par constructeur d'image expérimental |
| A500 | Kickstart 1.3 r34.005 (262144 octets) | À fournir légalement |
| A1200 | Kickstart 3.1 r40.068 (524288 octets) | À fournir légalement |
| A600 | Kickstart 2.05 r37.350 | Optionnel |
| Amiga accéléré | ROM adaptée à la machine émulée, RTG/JIT | À sélectionner/tester |
| Workbench | Disquettes système AmigaOS compatibles avec la ROM | À fournir légalement |
| Jeux | ADF, ADZ, IPF, WHDLoad en LHA | Bibliothèque utilisateur |
| Stockage | HDF, HDZ, répertoires hôtes | Génération/configuration utilisateur |
| CD | ISO et CUE | Futur profil CD32 |
| Contrôleurs | Config SDL/Amiberry | À calibrer |
| Présentation | Icônes, captures, thèmes avec licences adaptées | Étape ultérieure |

## Sources de métadonnées à étudier
- [Amiberry Kickstart ROMs](https://github.com/BlitterStudio/amiberry/wiki/Kickstart-ROMs-%28BIOS%29) : compatibilité/CRC32/nom.
- [libretro-database System.dat](https://github.com/libretro/libretro-database/blob/master/dat/System.dat) : empreintes BIOS.
- [libretro-uae README](https://github.com/libretro/libretro-uae/blob/master/README.md) : modèles, noms et empreintes.
- [Hall of Light](https://amiga.abime.net/) : information éditoriale jeux ; vérifier conditions d'accès et réutilisation avant un connecteur.
- [Lemon Amiga](https://www.lemonamiga.com/) : métadonnées communautaires ; pas de scraping sans conditions et limites vérifiées.
- [WHDLoad](https://www.whdload.de/) : documentation et installations.
- TOSEC DAT : utiliser des fichiers de catalogage sous conditions de licence, pas des paquets de jeux.

## Pipeline cible
1. **Scan local** : découverte de fichiers par extension et lecture en blocs.
2. **Hash** : SHA-1, SHA-256, CRC32 ; taille et extension ; lecture seule.
3. **Identification certaine** : correspondance exacte avec base de checksums, jamais sur simple nom.
4. **Enrichissement optionnel** : importer DAT autorisés ou consulter une API avec cache, attribution, délai et consentement.
5. **Bibliothèque SQLite** : chemin, empreintes, type, identification, statut et historique.
6. **Audit compatibilité** : manque-t-il Kickstart 1.3, 3.1, Workbench, profils?
7. **UI ROM Center** : interface locale Web/Python, favoris, jaquettes licenciées, filtres, doublons, synchronisation avec Amiberry.

## Prototype livré
`tools/azrom.py` est un scanner **hors réseau et en lecture seule sur les médias**. Il peut écrire un export JSON ou une base SQLite à la demande. Aucune décompression d'archives ou inspection de contenu interne complexe à ce stade. La reconnaissance inclut quatre SHA-1 publics de Kickstart courants ; les autres médias resteront *unidentified* jusqu'à import d'une base DAT.

```bash
python3 tools/azrom.py /chemin/vers/mes/fichiers --db local/az-miga.db --json local/inventaire.json
python3 -m unittest discover -s tests -v
```

Le répertoire `local/` est exclu de Git. Ne jamais lancer l'outil sur une bibliothèque qui ne vous appartient pas sans permission.

## DSI 10 pouces
La gestion DSI est indépendante du catalogue de ROM. Elle reste en attente de la référence exacte de l'écran et d'un test physique.
