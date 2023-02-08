import requests
import urllib.request
from bs4 import BeautifulSoup


def get_links(url):
    website = requests.get(url)
    website_text = website.text
    soup = BeautifulSoup(website_text, features="html.parser")

    for link in soup.find_all('a'):
        link = link.get("href")
        link = ('https://www.hdcarwallpapers.com/walls' + link).replace('-wallpapers', '-HD.jpg')
        if link not in exclude:
            links.append(link)

    for link in links:    
        print(link)

    print(f'''{"=" * 50}
    Links encontrados: {len(links)}
{"=" * 50}''')
    

def downloader(links):
    for link in links:
        print(f'Downloading: {link}')
        print('=' * 50)  
        pictureName = link.replace('https://www.hdcarwallpapers.com/walls/', '')      
        urllib.request.urlretrieve(link, f"D:\Pictures\Wallpapers\HD Cars Wallpapers\{pictureName}")       

page = int(input('Number of start page: '))
while True:    
    if page == 1:
        url = 'https://www.hdcarwallpapers.com/'
    if page > 1:
        url = (f'https://www.hdcarwallpapers.com/latest_wallpapers?page={page}') 
    links = []
    exclude = [
    'https://www.hdcarwallpapers.com/walls/',
    'https://www.hdcarwallpapers.com/walls#',
    'https://www.hdcarwallpapers.com/walls/',
    'https://www.hdcarwallpapers.com/walls/latest_wallpapers',
    'https://www.hdcarwallpapers.com/walls#',
    'https://www.hdcarwallpapers.com/walls/top_download_wallpapers/trending',
    'https://www.hdcarwallpapers.com/walls/top_view_wallpapers/trending',
    'https://www.hdcarwallpapers.com/walls#',
    'https://www.hdcarwallpapers.com/walls/1920x1080-hd-HD.jpg-r',
    'https://www.hdcarwallpapers.com/walls/2560x1440-qhd-HD.jpg-r',
    'https://www.hdcarwallpapers.com/walls/3840x2160-4k-HD.jpg-r',
    'https://www.hdcarwallpapers.com/walls/5120x2880-5k-HD.jpg-r',
    'https://www.hdcarwallpapers.com/walls/7680x4320-ultra-hd-8k-HD.jpg-r',
    'https://www.hdcarwallpapers.com/walls/random_wallpapers',
    'https://www.hdcarwallpapers.com/wallshttps://play.google.com/store/apps/details?id=com.autoapps.carwallpapers',
    'https://www.hdcarwallpapers.com/walls/latest_wallpapers?page=2',
    'https://www.hdcarwallpapers.com/walls/latest_wallpapers?page=2',
    'https://www.hdcarwallpapers.com/walls/acura-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/alfa_romeo-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/aston_martin-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/audi-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/bentley-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/bmw-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/bugatti-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/cadillac-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/chevrolet-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/citroen-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/dodge-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/ferrari-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/ford-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/fiat-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/genesis-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/honda-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/hummer-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/hyundai-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/infiniti-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/jaguar-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/jeep-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/kia-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/koenigsegg-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/lamborghini-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/land_rover-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/lexus-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/lincoln-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/lotus-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/maserati-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/maybach-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/mazda-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/mclaren-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/mercedes_benz-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/mini-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/mitsubishi-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/nissan-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/noble-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/opel-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/pagani-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/peugeot-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/pininfarina-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/polestar-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/renault-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/rolls_royce-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/skoda-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/tesla-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/toyota-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/volkswagen-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/volvo-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/zenvo-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/walls/other_cars-desktop-HD.jpg',
    'https://www.hdcarwallpapers.com/wallshttps://play.google.com/store/apps/details?id=com.autoapps.carwallpapers',
    'https://www.hdcarwallpapers.com/walls/privacy',
    'https://www.hdcarwallpapers.com/walls/contact',
    'https://www.hdcarwallpapers.com/walls/contact',
    'https://www.hdcarwallpapers.com/walls/privacy',
    'https://www.hdcarwallpapers.com/wallsjavascript:void(0)',
    'https://www.hdcarwallpapers.com/walls/latest_wallpapers?']

    get_links(url)
    downloader(links)
    page += 1
