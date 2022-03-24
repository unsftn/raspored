#!/bin/python
import re
import requests
from requests_html import HTMLSession

FTN_SITE = "http://ftn.uns.ac.rs"
ROOT_PAGE = f"{FTN_SITE}/1344336623/raspored-nastave-za-letnji-semestar-2021-2022-novi-od-11-04-2022-"

pdfs = {
    "animacija-u-inzenjerstvu": "ani.pdf",
    "arhitektura": "arh.pdf",
    "biomedicinsko-inzenjerstvo": "bio.pdf",
    "ciste-energetske-tehnologije": "cet.pdf",
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
    "scenska-arhitektura-i-dizajn": "sce.pdf",
    "softversko-inzenjerstvo-i-informacione-tehnologije": "sit.pdf",
    "upravljanje-rizikom-od-katastrofalnih-dogadjaja-i-pozara": "upr.pdf",
    "vestacka-inteligencija-i-masinsko-ucenje": "vei.pdf",
    "oss-elektrotehnika": "OSSEOS.pdf",
    "oss-elektroenergetika-obnovljivi-izvori-elektricne-energije": "OSSEET.pdf",
    "oss-elektronika-i-telekomunikacije": "OSSET.pdf",
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


# pdfs = [
#     ("http://ftn.uns.ac.rs/802448994/animacija-u-inzenjerstvu", "ani.pdf"),
#     ("http://ftn.uns.ac.rs/802448995/arhitektura", "arh.pdf"),
#     ("http://ftn.uns.ac.rs/802448996/biomedicinsko-inzenjerstvo", "bio.pdf"),
#     ("http://ftn.uns.ac.rs/802448997/ciste-energetske-tehnologije", "cet.pdf"),
#     ("http://ftn.uns.ac.rs/802448998/energetika--elektronika-i-telekomunikacije", "eet.pdf"),
#     ("http://ftn.uns.ac.rs/802448999/geodezija-i-geoinformatika", "geo.pdf"),
#     ("http://ftn.uns.ac.rs/802449000/graficko-inzenjerstvo-i-dizajn", "gi.pdf"),
#     ("http://ftn.uns.ac.rs/802449001/gradjevinarstvo", "gr.pdf"),
#     ("http://ftn.uns.ac.rs/802449002/industrijsko-inzenjerstvo", "ii.pdf"),
#     ("http://ftn.uns.ac.rs/n893884914/inzenjerski-menadzment", "im.pdf"),
#     ("http://ftn.uns.ac.rs/n893884913/inzenjerstvo-informacionih-sistema", "iis.pdf"),
#     ("http://ftn.uns.ac.rs/n893884912/inzenjerstvo-inovacija", "inov.pdf"),
#     ("http://ftn.uns.ac.rs/n893884911/informacioni-inzenjering", "inz.pdf"),
#     ("http://ftn.uns.ac.rs/n893884910/informaciona-bezbednost", "inb.pdf"),
#     ("http://ftn.uns.ac.rs/n893884909/inzenjerstvo-tretmana-i-zastita-voda", "itv.pdf"),
#     ("http://ftn.uns.ac.rs/n893884908/inzenjerstvo-zastite-zivotne-sredine-i-zastite-na-radu", "izs.pdf"),
#     ("http://ftn.uns.ac.rs/n893884907/masinstvo", "mas.pdf"),
#     ("http://ftn.uns.ac.rs/n893884906/matematika-u-tehnici", "mat.pdf"),
#     ("http://ftn.uns.ac.rs/n893884905/mehatronika", "meh.pdf"),
#     ("http://ftn.uns.ac.rs/n893884883/merenje-i-regulacija", "mer.pdf"),
#     ("http://ftn.uns.ac.rs/n893884882/planiranje-i-upravljanje-regionalnim-razvojem", "pla.pdf"),
#     ("http://ftn.uns.ac.rs/n893884881/primenjeno-softversko-inzenjerstvo", "pri.pdf"),
#     ("http://ftn.uns.ac.rs/n893884880/racunarstvo-i-automatika", "rac.pdf"),
#     ("http://ftn.uns.ac.rs/n893884879/saobracaj", "sao.pdf"),
#     ("http://ftn.uns.ac.rs/n893884878/scenska-arhitektura-i-dizajn", "sce.pdf"),
#     ("http://ftn.uns.ac.rs/n893884877/softversko-inzenjerstvo-i-informacione-tehnologije", "sit.pdf"),
#     ("http://ftn.uns.ac.rs/n893884876/upravljanje-rizikom-od-katastrofalnih-dogadjaja-i-pozara", "upr.pdf"),
#     ("http://ftn.uns.ac.rs/n893884875/vestacka-inteligencija-i-masinsko-ucenje", "vei.pdf"),
#     ("http://ftn.uns.ac.rs/n893884874/oss-elektrotehnika", "OSSEOS.pdf"),
#     ("http://ftn.uns.ac.rs/n893884852/oss-elektroenergetika-obnovljivi-izvori-elektricne-energije", "OSSEET.pdf"),
#     ("http://ftn.uns.ac.rs/n893884851/oss-elektronika-i-telekomunikacije", "OSSET.pdf"),
#     ("http://ftn.uns.ac.rs/n893884850/oss-softverske-informacione-tehnologije", "OSSSIT.pdf"),
#     ("http://ftn.uns.ac.rs/n893884849/mss-elektrotehnika", "MSSEMS.pdf"),
#     ("http://ftn.uns.ac.rs/n893884848/mss-inzenjerski-menadzment-mba", "MSSMBA.pdf"),
#     ("http://ftn.uns.ac.rs/n893884847/mss-proizvodno-masinstvo", "MSSPMS.pdf"),
# ]

# for pdf_url, pdf_name in pdfs:
#     pdf = requests.get(pdf_url)
#     with open(pdf_name, 'wb') as f:
#         f.write(pdf.content)
