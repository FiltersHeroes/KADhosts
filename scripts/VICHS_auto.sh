#!/bin/bash

# Sciezka to miejsce, w którym znajduje się skrypt
sciezka=$(dirname "$0")

cd $sciezka/..

if [ "$CI" = "true" ] ; then
    git config --global user.email "PolishJarvis@int.pl"
    git config --global user.name "PolishJarvis"
fi


$sciezka/VICHS.sh $sciezka/../KADhosts.txt
