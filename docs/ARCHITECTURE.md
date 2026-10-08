# Architecture AZ-miga

## Couches

```text
[Écran DSI 10 pouces]  [USB clavier/souris/manette]  [Audio]
                 \             |             /
             Raspberry Pi 4 / Raspberry Pi OS ARM64
                              |
                     Amiberry (SDL/KMS)
                              |
      +-----------------------+-----------------------+
      |                       |                       |
    A500 OCS/ECS          A1200 AGA          Amiga accéléré
    Kickstart 1.3         Kickstart 3.1        RTG/JIT (test)
      |                       |                       |
   ADF/jeux            Workbench/WHDLoad       Applications
```

## Décisions

- Démarrer depuis la session graphique locale pour le prototype ; étudier KMSDRM / kiosk seulement après validation DSI, saisie et audio.
- Ne pas inventer de résolution de panneau ; commencer par lire DRM et EDID quand disponible.
- Garder une configuration UAE par profil et une configuration de référence connue fonctionnelle.
- Stocker les fichiers de travail de l'utilisateur dans un répertoire local ignoré par Git.
- Prévoir sauvegardes cohérentes des disques virtuels, captures et profils.

## Phases d'intégration

1. Boot hôte + diagnostic écran/audio.
2. Amiberry et premier A500 avec média libre/licite.
3. A1200 AGA + installation Workbench depuis ses médias légitimes.
4. Profils, optimisation, compatibilité manettes.
5. Launcher local et boot direct avec bouton de maintenance.

## Performance : méthode

Vérifier la fluidité PAL 50 Hz, les craquements audio, la latence USB, les erreurs DRM, la température et le throttling CPU, en comparant options CPU, chipset exact, fréquence et rendu. Aucun score n'est présumé acquis.

## Limites

Workbench historique n'est pas conçu pour le multitouch ; l'usage tactile nécessitera un mapping fiable vers la souris. Les profils RTG/JIT et filtres CRT ne sont pas garantis sur toutes les charges.
