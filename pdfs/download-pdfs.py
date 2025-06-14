#!/bin/python
import re
import requests
from requests_html import HTMLSession

FTN_SITE = "https://ftn.uns.ac.rs"
ROOT_PAGE = f"{FTN_SITE}/wp-content/uploads/2025/06/"

pdfs = [
    # animacija-u-inzenjerstvu
    "ani-1.pdf",
    # arhitektura
    "arh.pdf",
    # biomedicinsko-inzenjerstvo
    "bio.pdf",
    # ciste-energetske-tehnologije
    "cet.pdf",
    # energetika--elektronika-i-telekomunikacije
    "eet.pdf",
    # geodezija-i-geoinformatika
    "geo.pdf",
    # graficko-inzenjerstvo-i-dizajn
    "gi.pdf",
    # gradjevinarstvo
    "gr.pdf",
    # industrijsko-inzenjerstvo
    "ii.pdf",
    # inzenjerski-menadzment
    "im.pdf",
    # inzenjerstvo-informacionih-sistema
    "iis.pdf",
    # informacioni-inzenjering
    "inz.pdf",
    # inzenjerstvo-zastite-zivotne-sredine-i-zastite-na-radu
    "izs.pdf",
    # masinstvo-proizvodno-masinstvo
    "masp.pdf",
    # masinstvo-mehanizacija-i-konstrukciono-masinstvo
    "masm.pdf",
    # masinstvo-energetika-i-procesna-tehnika
    "mase.pdf",
    # masinstvo-tehnicka-mehanizacija-i-dizajn-u-tehnici
    "mast.pdf",
    # mehatronika
    "meh.pdf",
    # merenje-i-regulacija
    "mer.pdf",
    # primenjeno-softversko-inzenjerstvo
    "pri.pdf",
    # racunarstvo-i-automatika
    "rac-3.pdf",
    # saobracaj
    "sao.pdf",
    # scenska-arhitektura
    "sce.pdf",
    # softversko-inzenjerstvo-i-informacione-tehnologije
    "sit.pdf",
    # upravljanje-rizikom-od-katastrofalnih-dogadjaja-i-pozara
    "upr.pdf",
    # oss-elektrotehnika
    "osseos.pdf",
    # oss-softverske-informacione-tehnologije
    "osssit.pdf",
    # mas-informaciona-bezbednost
    "inb.pdf",
    # mas-inzenjerstvo-tretmana-i-zastita-voda
    "itv.pdf",
    # mas-matematika-u-tehnici
    "mat.pdf",
    # mas-planiranje-i-upravljanje-regionalnim-razvojem
    "pla.pdf",
    # mas-vestacka-inteligencija-i-masinsko-ucenje
    "vei.pdf",
    # mss-elektrotehnika
    "mssems.pdf",
    # mss-inzenjerski-menadzment-mba
    "mssmba.pdf",
    # mss-proizvodno-masinstvo
    "msspms.pdf",
]

to_process = set(pdfs)

for file_name in pdfs:
    pdfr = requests.get(f'{ROOT_PAGE}{file_name}')
    with open(file_name, 'wb') as f:
        f.write(pdfr.content)
    to_process.remove(file_name)

if to_process:
    raise Exception(f'Linkovi za stud. programe {to_process} ne postoje.')
