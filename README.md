# raspored

Analiza i izveštavanje o rasporedu nastave i zauzeću prostorija na FTN-u

# Instalacija

Klonirajte repo i uradite sledeće u folderu projekta:

```
python -m venv venv
source venv/bin/activate
pip install -e .
```

# Generisanje izveštaja

U folderu `pdfs` nalazi se skripta za download pdf-ova sa FTN sajta. Na početku skripte se nalazi URL na stranicu sa rasporedima. Ažurirajte po potrebi.

Pokrenite skriptu da bi preuzeli nove pdf-ove:

```
cd pdfs
python download-pdfs.py
```

Zatim ih konvertujte u tekst. Potrebno je da imate dostupan u putanji
`ebook-convert` alat koji je deo `calibre`.

```
cd pdfs
./convert.sh
```

Biće kreiran fajl `all.raspored`. Ovo je ulaz za generator izveštaja.

Sada je moguće postavljati upite i kreirati izveštaje.

Na primer za puni izveštaj po učionicama i danima:

```
textx generate pdfs/all.raspored --target izvestaj > izvestaj/ucionice.txt
```

Ili ako je potrebno samo za određenog izvođača (može se navesti samo deo imena):

```
textx generate pdfs/all.raspored --target izvestaj --izvodjac dejanovi
```

Ili ako je potrebno samo za određenu učionicu (može se navesti samo deo imena):

```
textx generate pdfs/all.raspored --target izvestaj --ucionica 311
```

Izveštaj o predmetima i grupama po zadatim laboratorijama može se kreirati sa:

```
textx generate pdfs/all.raspored --target izvestajlabs --ucionice NTP-307,NTP-309,NTP-311,INT1,F315 > izvestaj/nase-laboratorije.txt
```


