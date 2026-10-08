# Roadmap ROM Center

## v0.1 : scanner local (sources publiées)
- [x] Parcours récursif de la bibliothèque, sans modification des médias.
- [x] Reconnaissance de types par extension.
- [x] Calcul SHA-1 / SHA-256 / CRC32.
- [x] Quatre entrées de firmware Kickstart identifiables par SHA-1.
- [x] Exports SQLite/JSON sur demande.
- [ ] Tests CI exécutés avec succès.

## v0.2 : bases de connaissance
- [ ] Chargeur DAT (XML Logiqx et éventuellement CLRMAMEPRO selon licence).
- [ ] Base normalisée de modèles Amiga, Kickstart requis, variantes.
- [ ] Identification multicritères et statut « inconnu » transparent.
- [ ] Détection de doublons et régionalisations.
- [ ] Rapport de ROM manquantes par profil.

## v0.3 : métadonnées
- [ ] Connecteurs facultatifs vers sources de métadonnées autorisées.
- [ ] Cache SQLite avec horodatage et attribution.
- [ ] Respect robots.txt, conditions d'utilisation, limitations de débit.
- [ ] Pas d'extraction de contenus protégés, pas de collecte à l'insu de l'utilisateur.
- [ ] Export d'un catalogue complet hors réseau.

## v0.4 : application locale
- [ ] Recherche et filtres, jacquettes quand la licence le permet.
- [ ] Import guidé des ROM en possession de l'utilisateur.
- [ ] Validation des profils Amiberry et contrôle des fichiers requis.
- [ ] Démarrage depuis le launcher AZ-miga.
- [ ] Sauvegarde et restauration.

## v1.0 : image intégrée
- [ ] Image pi-gen construite et testée sur vrai Pi 4.
- [ ] Scanner préinstallé, catalogues hors ligne.
- [ ] Assistant premier démarrage et interface adaptée au DSI.
- [ ] Amiberry A500/A1200 opérationnel et audio validé.

Les ROM/jeux ne font pas partie des livrables du dépôt.
