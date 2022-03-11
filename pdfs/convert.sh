#!/bin/sh
# Konvertuje pdf-ove u tekst. Koristi calibre (ebook-convert).

for f in *.pdf;
do
  ebook-convert "$f" "${f%.pdf}.txt"
done;

cat *.txt > all.raspored
