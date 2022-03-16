# raspored

Analiza i izveštavanje o rasporedu nastave i zauzeću prostorija na FTN-u

# Instalacija

```
python -m venv venv
source venv/bin/activate
pip install textX[cli]
```

# Generisanje izveštaja

Preuzmite pdf-ove rasporeda sa adrese http://ftn.uns.ac.rs/1344335571/raspored-nastave-za-letnji-semestar-2021-2022

i smestite ih u `pdfs` folder

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


