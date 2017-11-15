
import requests, os, bs4, shutil, sys
from pprint import pprint

modules = list(set(sys.modules) & set(globals()))
pprint(modules)

url1 = 'http://xkcd.com' # starting rule
url2 = 'https://github.com/paulrefalo'
url = url1
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
    comicURL = "http:"+comicElem[0].get('src')
    response = requests.get(comicURL, stream=True)
    with open('xkcd/img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response



print('Done.')