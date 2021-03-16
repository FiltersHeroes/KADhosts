#!/bin/bash

# SCRIPT_PATH to miejsce, w którym znajduje się skrypt
SCRIPT_PATH=$(dirname "$(realpath -s "$0")")

cd $SCRIPT_PATH/../..

if [[ "$CI" = "true" ]] && [[ -z "$CIRCLECI" ]] ; then
    git clone https://github.com/PolishFiltersTeam/KAD.git
fi
if [[ "$CI" = "true" ]] && [[ "$CIRCLECI" = "true" ]] ; then
    git clone git@github.com:PolishFiltersTeam/KAD.git
fi

cd ./KADhosts
./scripts/VICHS.sh ./KADhosts.txt ./KADhole.txt ./KADomains.txt
