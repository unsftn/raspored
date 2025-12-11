#!/bin/sh
# Konvertuje pdf-ove u tekst. Koristi calibre (ebook-convert).

for f in *.pdf;
do
  ebook-convert "$f" "${f%.pdf}.txt"
done;

cat *.txt | \

sed \
    -e 's/П О Н Е Д Е Љ А К/P O N E D E L J A K/g' \
    -e 's/љ/lj/g' \
    -e 's/Љ/Lj/g' \
    -e 's/њ/nj/g' \
    -e 's/Њ/Nj/g' \
    -e 's/џ/dž/g' \
    -e 's/Џ/Dž/g' \
    -e 'y/абвгдђежзијклљмнњопрстћуфхцчџш/abvgdđežzijkllmnnoprstćufhcčdš/' \
    -e 'y/АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ/ABVGDĐEŽZIJKLLMNNOPRSTĆUFHCČDŠ/' \
> all.raspored
