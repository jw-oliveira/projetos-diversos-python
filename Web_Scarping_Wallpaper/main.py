import requests
from bs4 import BeautifulSoup as bs

individual_pages = []


def find_page(url):
    r = requests.get(url)
    soup = bs(r.content, features='html.parser')
    image_names = soup.find_all('em1')


    for cont in range(0, len(image_names)):
        link = str(image_names[cont]).replace('<em1>', '').lower()
        link = link.replace('</em1>', '')
        link = link.replace(' ', '_')
        link = link.replace('.', '_')
        link = link.replace('-', '_')
        link = (f'https://www.hdcarwallpapers.com/walls/{link}-HD.jpg')
        
        individual_pages.append(link)


def export_to_txt(list_urls):
    with open(r'/Web_Scarping_Wallpaper/download_list.txt', 'w') as fp:
        for link in list_urls:
            # write each item on a new line
            fp.write("%s\n" % link)

     
url = str(input('Digite a URL: '))

find_page(url)
export_to_txt(individual_pages)


    












