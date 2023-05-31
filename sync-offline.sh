#!/usr/bin/env bash

sudo pacman -Syu --needed - < pkglist.txt
# pip install --no-index --find-links pip -r pypkg.txt

for extension in vsc-extensions/*.vsix; do
    code --install-extension $extension
done
