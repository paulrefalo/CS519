# -*- coding: utf-8 -*-
"""
Spyder Editor

xkcd dowloader
"""

import requests, os, bs4, shutil, sys
from pprint import pprint

modules = list(set(sys.modules) & set(globals()))
pprint(modules)

#cwd = os.getcwd()
#print(path)


print(cwd)
url = 'http://xkcd.com' # starting rule

if not os.path.exists('xkcd'):
    os.makedirs('xkcd') # store comics in ./xkcd

    # Download the page
print('Downloading the page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

# Find the URL of the comic image
comicElem = soup.select('#comic img')
if comicElem == []:
    print('Could not find comic image.')
else:
    comicUrl = 'https:' + comicElem[0].get('src')
    comicPath = comicElem[0].get('src')
    # Download the image.
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    print(res.raise_for_status())

#    r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
#    path = 'xkcd'
#    if r.status_code == 200:
#        with open(path, 'wb') as f:
#            for chunk in r.iter_content(1024):
#                f.write(chunk)
    # Save the image to ./xkcd
    print(comicPath)
    imageFile = open(os.path.join('xkcd', os.path.basename(comicPath)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
        
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')


print('Done.')

