#!/bin/bash
set -euo pipefail
rsync -avh --progress /mnt/kmtos/artifacts/actions-runner/ ./actions-runner/ || \
rsync -avh --progress /home/moghimi/kmtos-public-artifacts/actions-runner-archive/ ./actions-runner/
chown -R $(whoami):$(whoami) ./actions-runner
