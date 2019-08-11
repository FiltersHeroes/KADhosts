# KADhosts

Odpowiednik hosts dla filtra KAD.
Zalecany dla użytkowników zaawansowanych.

# Informacje

Oryginalne repozytorium KAD: https://github.com/PolishFiltersTeam/KAD

Lista hosts jest udostępniana na tej samej licencji co filtr - https://kadantiscam.netlify.com/#contact

Jeśli nie chcesz blokować sekcji [kontrowersyjnych stron](https://github.com/PolishFiltersTeam/KAD/issues/649), to zamiast listy [KADhosts](https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt) korzystaj z [KADhosts (bez kontrowersji)](https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts_without_controversies.txt).

Jeżeli korzystasz z **Pi-hole**, to polecamy również zainstalować dodatkową listę [KADhole](https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/scripts/KADhole.txt), blokującą więcej stron. Jednakże, aby działała ono prawidłowo, nie ściągaj listy samodzielnie, tylko pobierz [Instalator Regex Hosts do Pi-hole](https://raw.githubusercontent.com/PolishFiltersTeam/ScriptsPlayground/master/scripts/RHI_for_Pi-hole.sh), a następnie uruchom go z wpisanym adresem do listy jako jego parametrem, czyli `sciezka_do_instalatora/RHI_for_Pi-hole.sh https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/scripts/KADhole.txt`. Aktualizacje również należy przeprowadzać podobnie. Oczywiście można dodać ten skrypt do crona, by były automatycznie pobierane i instalowane co jakiś czas.
