import os
import datetime
from textx import language, generator, metamodel_from_file

__version__ = "0.1.0.dev"


@language('raspored', '*.raspored')
def raspored_language():
    "raspored language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'raspored.tx'))
    def izvođač_processor(obj):
        return obj.strip()
    def predmet_processor(obj):
        return obj.replace('\n', ' ')
    mm.register_obj_processors({'Izvođač': izvođač_processor,
                                'Predmet': predmet_processor})

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm

DANI = [
    'PONEDELJAK',
    'UTORAK',
    'SREDA',
    'ČETVRTAK',
    'PETAK',
    'SUBOTA'
]

@generator('raspored', 'izvestaj')
def generate_izvestaj(metamodel, model, output_path, overwrite, debug, **custom_args):
    termini_po_danima = {}
    termini_po_ucionicama = {}
    termini_blok_po_ucionicama = {}
    class Termin:
        def __init__(self, datum, od, do, predmet, ucionica):
            self.datum = datetime.date(*reversed([int(x) for x in datum.split('.')])) \
                if datum else None
            self.od = od
            self.do = do
            self.predmet = predmet
            self.ucionica = ucionica

    for semestar in model.semestri:
        for dan in semestar.termini_po_danima:
            for termin in dan.termin:
                included = True
                if 'izvodjac' in custom_args:
                    included = custom_args['izvodjac'].lower() in termin.predmet.lower()
                elif 'predmet' in custom_args:
                    included = custom_args['predmet'].lower() in termin.predmet.lower()
                elif 'ucionica' in custom_args:
                    included = custom_args['ucionica'].lower() in termin.učionica.lower()

                if included:
                    if dan.dan == 'BLOKNASTAVA':
                        assert termin.datum is not None
                        termini_blok_po_ucionicama.setdefault(termin.učionica, []).append(
                            Termin(termin.datum, termin.od, termin.do, termin.predmet, termin.učionica)
                        )
                    else:
                        termini_po_danima.setdefault(dan.dan, []).append(
                            Termin(None, termin.od, termin.do, termin.predmet, termin.učionica))
                        termini_po_ucionicama\
                            .setdefault(termin.učionica, {})\
                            .setdefault(dan.dan, []).append(
                            Termin(termin.datum, termin.od, termin.do, termin.predmet, termin.učionica))

    if custom_args:
        for dan, termini in sorted(termini_po_danima.items(), key=lambda x: DANI.index(x[0])):
            print(dan)
            for termin in sorted(termini, key=lambda x: x.od):
                print(f"\t{termin.od}-{termin.do}  {termin.ucionica}  {termin.predmet}")
    else:
        # Izveštaj po učionicama i danima
        for ucionica, dani in sorted(termini_po_ucionicama.items(), key=lambda x: x[0]):
            print(ucionica)
            for dan, termini in sorted(dani.items(), key=lambda x: DANI.index(x[0])):
                print(f"\t{dan}")
                for termin in sorted(termini, key=lambda x: x.od):
                    print(f"\t\t{termin.od}-{termin.do}  {termin.ucionica}  {termin.predmet}")
                if ucionica in termini_blok_po_ucionicama:
                    print("\t\tBLOK NASTAVA:")
                    dan_ord = DANI.index(dan)
                    for termin in sorted(filter(lambda x: x.datum.weekday() == dan_ord,
                                                termini_blok_po_ucionicama[ucionica]),
                                         key=lambda t: (t.od, t.datum)):
                        print(f"\t\t{termin.datum} {termin.od}-{termin.do}  {termin.ucionica}  {termin.predmet}")
