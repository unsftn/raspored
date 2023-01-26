#!/bin/python
import re
import requests
from requests_html import HTMLSession

FTN_SITE = "http://ftn.uns.ac.rs"
ROOT_PAGE = f"{FTN_SITE}/1344340502/raspored-nastave-za-letnji-semestar-skolske-2022-2023"

pdfs = {
    "animacija-u-inzenjerstvu": "ani.pdf",
    "arhitektura": "arh.pdf",
    "biomedicinsko-inzenjerstvo": "bio.pdf",
    "ciste-energetske-tehnologije": "cet.pdf",
    "digitalne-tehnike--dizajn-i-produkcija-u-arhitekturi": "dtdpa.pdf",
    "energetika--elektronika-i-telekomunikacije": "eet.pdf",
    "geodezija-i-geoinformatika": "geo.pdf",
    "graficko-inzenjerstvo-i-dizajn": "gi.pdf",
    "gradjevinarstvo": "gr.pdf",
    "industrijsko-inzenjerstvo": "ii.pdf",
    "inzenjerski-menadzment": "im.pdf",
    "inzenjerstvo-informacionih-sistema": "iis.pdf",
    "inzenjerstvo-inovacija": "inov.pdf",
    "informacioni-inzenjering": "inz.pdf",
    "informaciona-bezbednost": "inb.pdf",
    "inzenjerstvo-tretmana-i-zastita-voda": "itv.pdf",
    "inzenjerstvo-zastite-zivotne-sredine-i-zastite-na-radu": "izs.pdf",
    "masinstvo": "mas.pdf",
    "matematika-u-tehnici": "mat.pdf",
    "mehatronika": "meh.pdf",
    "merenje-i-regulacija": "mer.pdf",
    "planiranje-i-upravljanje-regionalnim-razvojem": "pla.pdf",
    "primenjeno-softversko-inzenjerstvo": "pri.pdf",
    "racunarstvo-i-automatika": "rac.pdf",
    "saobracaj": "sao.pdf",
    "scenska-arhitektura": "sce.pdf",
    "softversko-inzenjerstvo-i-informacione-tehnologije": "sit.pdf",
    "upravljanje-rizikom-od-katastrofalnih-dogadjaja-i-pozara": "upr.pdf",
    "vestacka-inteligencija-i-masinsko-ucenje": "vei.pdf",
    "oss-elektrotehnika": "OSSEOS.pdf",
    "oss-softverske-informacione-tehnologije": "OSSSIT.pdf",
    "mss-elektrotehnika": "MSSEMS.pdf",
    "mss-inzenjerski-menadzment-mba": "MSSMBA.pdf",
    "mss-proizvodno-masinstvo": "MSSPMS.pdf",
}

session = HTMLSession()

r = session.get(ROOT_PAGE)

to_process = set(pdfs)

for l in r.html.links:
    for studpr, file_name in list(pdfs.items()):
        if re.match(f'/[^/]*/{studpr}', l):
            pdfr = requests.get(f'{FTN_SITE}{l}')
            with open(file_name, 'wb') as f:
                f.write(pdfr.content)
            to_process.remove(studpr)

if to_process:
    raise Exception(f'Linkovi za stud. programe {to_process} ne postoje.')
