import requests
from bs4 import BeautifulSoup as bs

individual_pages = []


def title():
    print(f'{" DOWNLOADER DO SITE HDCARWALLPAPERS.COM ":=^50}')
    first_page = int(input('Digite o número da primeira página: '))
    last_page = int(input('Digite o número da última página: '))
    return first_page, last_page


def create_links(pages):
    first_page, last_page = pages
    for page in range(first_page, last_page + 1):
        r = requests.get(f'https://www.hdcarwallpapers.com/latest_wallpapers?page={page}')
        soup = bs(r.content, features='html.parser')
        image_names = soup.find_all('em1')

        for cont in range(0, len(image_names)):
            link = str(image_names[cont]).replace('<em1>', '').lower()
            link = link.replace('</em1>', '')
            link = link.replace(' ', '_')
            link = link.replace('.', '_')
            link = link.replace('-', '_')
            link = f'https://www.hdcarwallpapers.com/walls/{link}-HD.jpg'

            individual_pages.append(link)


def export_to_txt(list_urls):
    with open(r'download_list.txt', 'w') as fp:
        for link in list_urls:
            fp.write("%s\n" % link)


first_last_pages = title()
create_links(first_last_pages)
export_to_txt(individual_pages)
