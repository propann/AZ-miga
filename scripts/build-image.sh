#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$ROOT/.build"
mkdir -p "$BUILD"
[ -d "$BUILD/pi-gen/.git" ] || git clone --depth 1 https://github.com/RPi-Distro/pi-gen.git "$BUILD/pi-gen"
cd "$BUILD/pi-gen"
cat >config <<EOF
IMG_NAME='AZ-miga-pi4'
RELEASE='trixie'
ARCH='arm64'
PI_GEN_RELEASE='AZ-miga experimental'
STAGE_LIST='stage0 stage1 stage2 stage3 $ROOT/image/stage-azmiga stage4'
ENABLE_CLOUD_INIT=1
ENABLE_SSH=0
DEPLOY_ZIP=1
EOF
./build-docker.sh
echo "See $BUILD/pi-gen/deploy/"
