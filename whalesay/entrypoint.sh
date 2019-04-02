#!/bin/bash

#
#   Defina o arquivo como executável com: chmod +x entrypoint.sh
#

if [ $# -eq 0 ]; then
    /usr/games/cowsay -f `ls /usr/share/cowsay/cows/whale.cow` \
    `usr/games/fortune /usr/share/games/fortunes/brasil`
else
    /usr/games/cowsay -f `ls /usr/share/cowsay/cows/whale.cow` "$@"
fi