#!/usr/bin/env bash

# shellcheck disable=SC2046,SC2086
cd $(dirname $(realpath $0)) || exit

pip download -d pip --prefer-binary -r pypkg.txt
