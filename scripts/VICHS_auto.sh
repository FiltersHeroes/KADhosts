#!/bin/bash

# Sciezka to miejsce, w którym znajduje się skrypt
sciezka=$(dirname "$0")

cd $sciezka/..

$sciezka/VICHS.sh $sciezka/../KADhosts.txt
