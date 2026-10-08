#!/usr/bin/env bash
set -u
printf '%s\n' '=== AZ-miga : diagnostic lecture seule ==='
printf '\n[Machine]\n'
if [ -r /proc/device-tree/model ]; then tr -d '\000' < /proc/device-tree/model; echo; fi
uname -a
printf '\n[OS]\n'
if [ -r /etc/os-release ]; then grep -E '^(PRETTY_NAME|VERSION_CODENAME)=' /etc/os-release; fi
printf '\n[RAM]\n'
free -h 2>/dev/null || true
printf '\n[DRM]\n'
ls -l /dev/dri 2>/dev/null || true
for s in /sys/class/drm/*/status; do
  [ -f "$s" ] || continue
  printf '%s: ' "$s"
  cat "$s"
done
printf '\n[Framebuffer]\n'
fbset -s 2>/dev/null || true
printf '\n[Audio]\n'
aplay -l 2>/dev/null || true
printf '\n[Température et throttling]\n'
vcgencmd measure_temp 2>/dev/null || true
vcgencmd get_throttled 2>/dev/null || true
printf '\n[Interfaces]\n'
ls /sys/bus/i2c/devices 2>/dev/null | head -20 || true
printf '\n=== Fin diagnostic ===\n'
