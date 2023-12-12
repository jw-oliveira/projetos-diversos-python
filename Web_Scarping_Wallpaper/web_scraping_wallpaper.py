import requests
import re
from bs4 import BeautifulSoup as bs

individual_pages = []


def title():
    print(f'{" LINK GENERATOR - HDCARWALLPAPERS.COM ":=^50}')
    first_page = int(input('Digite o número da primeira página: '))
    last_page = int(input('Digite o número da última página: '))
    return first_page, last_page


def create_links(pages):
    first_page, last_page = pages
    for page in range(first_page, last_page + 1):
        r = requests.get(f'https://www.hdcarwallpapers.com/latest_wallpapers?page={page}')
        soup = bs(r.content, features='html.parser')
        image_names = soup.find_all('em1')

        for name in image_names:
            generate = re.sub(r'<em1>|</em1>', '', re.sub(r'\s+|-|\.', '_', str(name).lower()))
            generated_link = f'https://www.hdcarwallpapers.com/walls/{generate}-HD.jpg'
            individual_pages.append(generated_link)


def export_to_txt(list_urls):
    with open(r'download_list.txt', 'w') as fp:
        for link in list_urls:
            fp.write("%s\n" % link)


first_last_pages = title()
create_links(first_last_pages)
export_to_txt(individual_pages)
