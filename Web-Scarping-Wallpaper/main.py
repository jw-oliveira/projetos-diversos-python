import requests
from PIL import Image
from bs4 import BeautifulSoup as bs


individual_pages = []


def find_page():
    url = 'https://www.hdcarwallpapers.com/latest_wallpapers?page=2'
    r = requests.get(url)
    soup = bs(r.content, features='html.parser')
    image_names = soup.find_all('em1')


    for cont in range(0, len(image_names)):
        link = str(image_names[cont]).replace('<em1>', '').lower()
        link = link.replace('</em1>', '')
        link = link.replace(' ', '_')
        link = (f'https://www.hdcarwallpapers.com/walls/{link}-HD.jpg')
        
        individual_pages.append(link)


def downloader(pages):    
    url = pages[5]
    img = Image.open(requests.get(url, stream=True).raw)
    img.save('picture.jpg')
     
   
find_page()
downloader(individual_pages)



    












