#!/bin/bash -e
install -d -m 0755 "${ROOTFS_DIR}/usr/local/bin" "${ROOTFS_DIR}/usr/local/share/az-miga" "${ROOTFS_DIR}/etc/xdg/autostart"
install -m 0755 files/az-miga-launch.sh "${ROOTFS_DIR}/usr/local/bin/az-miga-launch"
install -m 0644 files/az-miga.desktop "${ROOTFS_DIR}/etc/xdg/autostart/az-miga.desktop"
install -m 0644 files/README-first-boot.txt "${ROOTFS_DIR}/usr/local/share/az-miga/README-first-boot.txt"
on_chroot <<'EOF'
set -eu
apt-get update
apt-get install -y --no-install-recommends curl ca-certificates gnupg
curl -fsSL https://packages.amiberry.com/install.sh -o /tmp/amiberry-repo.sh
sh /tmp/amiberry-repo.sh
apt-get update
apt-get install -y --no-install-recommends amiberry
rm -f /tmp/amiberry-repo.sh
EOF
