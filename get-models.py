import requests
from bs4 import BeautifulSoup as bs
import os

#website url
#url = 'https://www.pexels.com/search/model'
url = 'https://www.imgmodels.com/new-york/women'

page = requests.get(url)
soup = bs(page.text, 'html.parser')

image_tags = soup.findAll('img')
#print(image_tags)

if not os.path.exists('models'):
    os.makedirs('models')

#move to new directory
os.chdir('models')

x = 0
print(f"X is {x}")
for image in image_tags:
    #print("image src")
    print (image.get('data-original'))
    #print (image['alt'])
   
    try:
        url = image.get('data-original')
        source = requests.get(url)
        if source.status_code == 200:
            with open('model-'+str(x)+'.jpg','wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
                print(f"x is {x}")
    except OSError as err:
        print(f"Something not working {err}")
       