import pdfplumber
import glob
import os

def is_inside_box(word_box, table_box):
    x0, top, x1, bottom = word_box
    tb_x0, tb_y0, tb_x1, tb_y1 = table_box
    return (x0 >= tb_x0 and x1 <= tb_x1 and top >= tb_y0 and bottom <= tb_y1)


def custom_replace(text):
    replacements = {
        "П О Н Е Д Е Љ А К": "P O N E D E L J A K",
        "љ": "lj",
        "Љ": "Lj",
        "њ": "nj",
        "Њ": "Nj",
        "џ": "dž",
        "Џ": "Dž",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def convert_cyrillic_to_latin(text):
    
    lower_map = str.maketrans(
        "абвгдђежзијклљмнњопрстћуфхцчџш",
        "abvgdđežzijkllmnnoprstćufhcčdš"
    )
    upper_map = str.maketrans(
        "АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ",
        "ABVGDĐEŽZIJKLLMNNOPRSTĆUFHCČDŠ"
    )
    
    text = custom_replace(text)
    text = text.translate(lower_map)
    text = text.translate(upper_map)
    return text
    
    return text.translate(translation_table)

output_path = "pdfs/all.raspored"
with open(output_path, "w", encoding="utf-8") as out:

    for path in glob.glob("pdfs/*.pdf"):
        print(f"Opening: {path}")
        with pdfplumber.open(path) as pdf:
            filename = os.path.basename(path).split("-")[0]
            out.write("filename:" + filename + " ")
            
            for page_index, page in enumerate(pdf.pages, start=1):
                tables = page.find_tables()
                table_boxes = [t.bbox for t in tables]

                words = page.extract_words()

                non_table_words = []
                for w in words:
                    word_box = (w["x0"], w["top"], w["x1"], w["bottom"])
                    if not any(is_inside_box(word_box, box) for box in table_boxes):
                        non_table_words.append(w["text"])

                if non_table_words:
                    out.write(convert_cyrillic_to_latin(" ".join(non_table_words) + "\n"))

                if tables:
                    for t_index, table in enumerate([t.extract() for t in tables], start=1):
                        for row in table:
                            line = " ".join((cell or "").replace("\n", " ") for cell in row)
                            out.write(convert_cyrillic_to_latin(line) + "\n")
                            
            out.write("\n\n")
