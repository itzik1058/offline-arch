#!/usr/bin/env bash

# shellcheck disable=SC2046,SC2086
cd $(dirname $(realpath $0)) || exit

sudo pacman -Syw --cachedir ./pacman --dbpath ./pacman/db --noconfirm - < pkglist.txt
sudo pacman -Syw --cachedir ./pacman --dbpath ./pacman/db --noconfirm - < pkglist-aur.txt
cp -v ./aur/**/*.zst ./pacman/
sudo repo-add -n ./pacman/custom.db.tar.gz ./pacman/*.zst
