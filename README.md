# KADhosts

[![Issues h](https://isitmaintained.com/badge/resolution/FiltersHeroes/KADhosts.svg)](https://github.com/FiltersHeroes/KADhosts/issues)
[![Issues o](https://img.shields.io/github/issues/FiltersHeroes/KADhosts.svg?colorB=23b69a)](https://github.com/FiltersHeroes/KADhosts/issues)
[![repo size](https://img.shields.io/github/repo-size/FiltersHeroes/KADhosts.svg?colorB=23b69a)](https://github.com/FiltersHeroes/KADhosts)


Odpowiednik hosts dla filtrów KAD.
Zalecany dla użytkowników zaawansowanych.

# Informacje

Oryginalne repozytorium KAD: https://github.com/FiltersHeroes/KAD

Lista hosts jest udostępniana na tej samej licencji co filtry - https://kadantiscam.netlify.app/#contact

Jeżeli korzystasz z **Pi-hole**, to polecamy również zainstalować dodatkową listę [KADhole](https://raw.githubusercontent.com/FiltersHeroes/KADhosts/master/KADhole.txt), blokującą więcej stron. Jednakże, aby działała ono prawidłowo, nie ściągaj listy samodzielnie, tylko pobierz [Instalator Regex Hosts do Pi-hole](https://raw.githubusercontent.com/FiltersHeroes/ScriptsPlayground/master/scripts/RLI_for_Pi-hole.py), a następnie uruchom go z wpisanym adresem do listy jako jego parametrem, czyli `sciezka_do_instalatora/RLI_for_Pi-hole.py https://raw.githubusercontent.com/FiltersHeroes/KADhosts/master/KADhole.txt`. Aktualizacje również należy przeprowadzać podobnie. Oczywiście można dodać ten skrypt do crona, by były automatycznie pobierane i instalowane co jakiś czas.

# Używanie listy HOSTS z pomocą DNS

Niektóre DNS-y używają naszych list **KAD** w formacie hosts oraz domenowym i można je alternatywnie używać (np. na urządzeniach mobilnych). Są to między innymi:

* [nextdns.io](https://nextdns.io/) (zawiera bezpośrednio listę **KADomeny** w domyślnej konfiguracji, opcjonalnie można włączyć „blokowanie nowo zarejestrowanych domen (NRD)”),
* [libredns.gr](https://libredns.gr/) (wersja z aktywnym adblockiem, bazuje na [StevenBlack hosts](https://github.com/StevenBlack/hosts).
