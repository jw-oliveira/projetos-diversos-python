import urllib.request as urlib
from time import sleep


def urlTest(url):
    print('Checking connectivity...')
    sleep(2)
    print('-' * 50)

    response = urlib.urlopen('https://' + url)
    
    try:        
        print(f'Connected to {url} succefully')
        print('The response code was: ', response.getcode())
    except:
        print('Site connectivity error.')        
    
    print('-' * 50)


print(f'=' * 50)
print(f'{"Site connectivity test":^50}')
print(f'=' * 50)
inputURL = str(input('Input the url of the site: '))

urlTest(inputURL)


    
   

