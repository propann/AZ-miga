#!/bin/sh
# READ ONLY — does not change drivers, mapping or boot overlays.
set -u
echo "=== AZ-miga touch / DSI diagnostics ==="
echo "[Model]"
tr -d '\000' </proc/device-tree/model 2>/dev/null || true
echo
echo "[Kernel]"
uname -a
echo "[Session]"
printf 'Type=%s Desktop=%s\n' "${XDG_SESSION_TYPE:-unknown}" "${XDG_CURRENT_DESKTOP:-unknown}"
echo "[DRM devices]"
ls -l /dev/dri 2>/dev/null || true
echo "[Output connectors]"
for d in /sys/class/drm/*; do
  [ -f "$d/status" ] || continue
  printf '%s: ' "$d"; cat "$d/status"
  [ -r "$d/modes" ] && head -10 "$d/modes"
done
echo "[Input devices]"
cat /proc/bus/input/devices 2>/dev/null || true
echo "[libinput]"
if command -v libinput >/dev/null 2>&1; then libinput list-devices 2>/dev/null || true; fi
echo "[i2c]"
ls /dev/i2c-* 2>/dev/null || true
echo "[vcgencmd]"
command -v vcgencmd >/dev/null 2>&1 && vcgencmd get_throttled || true
echo "=== end ==="
