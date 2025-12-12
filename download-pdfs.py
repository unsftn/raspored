import os
from itertools import chain
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

# Korenski URL za stranicu sa rasporedima
url = 'https://ftn.uns.ac.rs/raspored-i-realizacija-2'

pdf_dir = 'pdfs'
os.makedirs(pdf_dir, exist_ok=True)

for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        file_path = os.path.join(pdf_dir, filename)
        os.remove(file_path)


def get_filename_from_headers(response, default_name):
    '''
    Extract filename from the HTTP headers
    '''
    content_disposition = response.headers.get('Content-Disposition')
    if content_disposition:
        parts = content_disposition.split(';')
        for part in parts:
            if 'filename=' in part:
                filename = part.split('=')[1].strip().strip('"')
                return filename
    return default_name

response = requests.get(url)
if response.status_code == 200:
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    # Prvi `li` od koga krećemo ekstrakciju
    start_a = soup.find('a', href=re.compile(r'ani-\d+\.pdf'))
    start_li = start_a.parent if start_a else None

    hrefs = []
    if start_li:
        for li in chain([start_li], start_li.next_siblings):
            link = li.find('a')
            if link and link['href']:
                full_url = requests.compat.urljoin(url, link['href'])
                hrefs.append(full_url)

    print("Extracted hrefs:", hrefs)

    for i, href in enumerate(hrefs):
        try:
            response = requests.get(href)
            if response.status_code == 200:
                parsed_url = urlparse(href)
                default_pdf_name = f'document_{i + 1}.pdf'
                filename = get_filename_from_headers(response, os.path.basename(parsed_url.path) or default_pdf_name)
                pdf_filename = os.path.join(pdf_dir, filename)

                with open(pdf_filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded and saved: {pdf_filename}")
            else:
                print(f"Failed to download {href}: {response.status_code}")
        except Exception as e:
            print(f"Error processing {href}: {e}")
else:
    print(f"Failed to fetch the URL: {url}, Status code: {response.status_code}")
