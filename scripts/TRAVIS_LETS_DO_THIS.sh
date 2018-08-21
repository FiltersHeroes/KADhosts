#!/bin/bash

# Sciezka to miejsce, w którym znajduje się skrypt
sciezka=$(dirname "$0")

cd $sciezka/..

$sciezka/VICHS_Travis.sh $sciezka/../KADhosts.txt
