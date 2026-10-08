# Étude des solutions open source — 2026-10-08

## Sélection

| Projet | Source | Intérêt pour AZ-miga | Stratégie |
|---|---|---|---|
| Amiberry | https://github.com/BlitterStudio/amiberry | Émulateur natif ARM64, ADF, WHDLoad, JIT/RTG | Installer comme dépendance externe, ne pas copier |
| Amiberry Lite | https://github.com/BlitterStudio/amiberry-lite | Alternative pour machine lente | Benchmark de repli |
| PiMIGA | https://www.pimiga.com/ | Inspiration pour poste Amiga prêt à l'emploi | Étudier l'expérience, ne pas redistribuer l'image |
| RetroPie | https://github.com/RetroPie/RetroPie-Setup | Frontend et gestion périphériques rétro | Référence secondaire |
| Batocera | https://github.com/batocera-linux/batocera.linux | Distribution console, approche plein écran | Comparatif de compatibilité, pas base retenue |
| AROS | https://aros.sourceforge.io/ | OS libre apparenté à AmigaOS | Expérimentation distincte |
| WHDLoad | https://www.whdload.de/ | Jeux installés sur disque | Utiliser selon licence et conditions |
| Raspberry Pi firmware overlays | https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README | Identifier le support DSI | Vérifier l'overlay exact |

## Conclusion

**Raspberry Pi OS ARM64 + Amiberry** apporte la meilleure flexibilité pour l'intégration DSI, l'usage Workbench et la maintenance SSH. Amiberry-Lite sert de recours si certaines charges sont trop lourdes. Les distributions console sont inadaptées comme fondation principale d'un ordinateur Amiga polyvalent.

## Recherches confirmées

- Quick start Amiberry mis à jour en août 2026 : https://github.com/BlitterStudio/amiberry/wiki/Quick-start-guide
- Dépôt de paquets : https://packages.amiberry.com/
- Compilation : https://github.com/BlitterStudio/amiberry/wiki/Compile-from-source
- Overlays DSI maintenus : https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README

## Contrôle avant réutilisation de code

Vérifier le dépôt d'origine, la licence actuelle du fichier ciblé, sa provenance, les dépendances, sa maintenance et sa compatibilité ARM64. Préférer installer ou interfacer un projet, plutôt que recopier ses composants. Ne pas importer d'images préconfigurées intégrant du contenu propriétaire.

## Questions à tester physiquement

- Rendu plein écran Amiberry SDL3 sur l'écran DSI 10 pouces.
- Compatibilité KMSDRM et gestion de rotation.
- PAL 50 Hz vs rafraîchissement réel de la dalle.
- Profil A1200 AGA et qualité audio.
- Différence réelle Amiberry vs Lite sur le Pi 4.
