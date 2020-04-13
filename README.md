# KADhosts

[![Issues h](https://isitmaintained.com/badge/resolution/PolishFiltersTeam/KADhosts.svg)](https://github.com/PolishFiltersTeam/KADhosts/issues)
[![Issues o](https://img.shields.io/github/issues/PolishFiltersTeam/KADhosts.svg?colorB=23b69a)](https://github.com/PolishFiltersTeam/KADhosts/issues)


Odpowiednik hosts dla filtrów KAD.
Zalecany dla użytkowników zaawansowanych.

# Informacje

Oryginalne repozytorium KAD: https://github.com/PolishFiltersTeam/KAD

Lista hosts jest udostępniana na tej samej licencji co filtry - https://kadantiscam.netlify.com/#contact

Jeżeli korzystasz z **Pi-hole**, to polecamy również zainstalować dodatkową listę [KADhole](https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhole.txt), blokującą więcej stron. Jednakże, aby działała ono prawidłowo, nie ściągaj listy samodzielnie, tylko pobierz [Instalator Regex Hosts do Pi-hole](https://raw.githubusercontent.com/PolishFiltersTeam/ScriptsPlayground/master/scripts/RLI_for_Pi-hole.sh), a następnie uruchom go z wpisanym adresem do listy jako jego parametrem, czyli `sciezka_do_instalatora/RLI_for_Pi-hole.sh https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhole.txt`. Aktualizacje również należy przeprowadzać podobnie. Oczywiście można dodać ten skrypt do crona, by były automatycznie pobierane i instalowane co jakiś czas.

Od niedawna dostępna jest również dodatkowa lista [KADfake Hosts Edition](https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADfakeHosts.txt), która blokuje pseudonaukę, dezinformację, nieprawdziwe informacje i kontrowersyjne strony bez polityki i satyry (https://github.com/PolishFiltersTeam/KAD/issues/649).
