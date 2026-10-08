# Matériel Raspberry Pi 4 / DSI 10 pouces

## Confirmé par le projet

- Raspberry Pi 4.
- Écran annoncé DSI de 10 pouces.

## Inconnu — relevé obligatoire

- Marque et référence de la dalle/contrôleur.
- Résolution native, orientation et fréquences supportées.
- Type de nappe, carte d'interface éventuelle, alimentation indépendante, rétroéclairage.
- Fonction tactile, interface I2C/USB et calibration.
- Mémoire RAM Pi 4, alimentation et stockage disponibles.

## Consignes

NE PAS insérer au hasard un `dtoverlay` dans `/boot/firmware/config.txt`. Des overlays 10,1 pouces existent (notamment plusieurs Waveshare), mais ne sont pas interchangeables. Consulter https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README et la notice fabricant exacte.

## Commandes de diagnostic non destructif

```bash
cat /proc/device-tree/model 2>/dev/null; echo
uname -m
cat /etc/os-release
ls -l /dev/dri/ 2>/dev/null
find /sys/class/drm -maxdepth 2 -name status -exec sh -c 'echo "$1: $(cat "$1")"' _ {} \;
vcgencmd get_throttled 2>/dev/null || true
```

## Validation DSI

1. Affiche un bureau sans écran HDMI auxiliaire.
2. Résolution et orientation correctes.
3. Tactile calibré si présent.
4. Redémarrage fiable et rétroéclairage stable.
5. Test Amiberry et audio simultanés.
