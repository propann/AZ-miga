#!/bin/sh
# Launch setup GUI, not a fictional pre-installed Workbench.
command -v amiberry >/dev/null 2>&1 && exec amiberry
echo 'Amiberry unavailable' >&2
exit 1
