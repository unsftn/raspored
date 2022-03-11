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

Zatim ih konvertujte u tekst upotrebom. Potrebno je da imate dostupan u putanji `ebook-convert` alat koji je deo `calibre`.

```
cd pdfs
./convert.sh
```

Biće kreiran fajl `all.raspored`. Ovo je ulaz za generator izveštaja.

Sada je moguće postavljati upite i kreirati izveštaje.

Na primer za puni izveštaj po učionicama i danima:

```
textx generate pdfs/all.raspored --target izvestaj > izvestaji/ucionice.txt
```

Ili ako je potrebno samo za određenog izvođača (navodi se deo imena):

```
textx generate pdfs/all.raspored --target izvestaj --izvodjac dejanovi
```

Ili ako je potrebno samo za određenu učionicu (navodi se deo imena):

```
textx generate pdfs/all.raspored --target izvestaj --ucionica 311
```


