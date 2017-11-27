#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
# OSU CS 519
# by Paul ReFalo 17 Nov 2017

import requests, os, bs4, threading, sys, timeit
from pprint import pprint

# modules = list(set(sys.modules) & set(globals()))
# pprint(modules)
#
# cwd = os.getcwd()
# print(cwd)

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        #print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            # comicUrl = comicElem[0].get('src')
            comicUrl = 'https:' + comicElem[0].get('src')

            # Download the image.
            #print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

def manageThreads(comics, threads):
    segments = int(comics / threads)
    # Create and start the Thread objects.
    start = timeit.default_timer()

    downloadThreads = [] # a list of all the Thread objects
    # was range(0, 1400, 100)
    for i in range(101, 101 + comics, segments): # loops comics/threads times, creates the number of threads
        downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + segments))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    # Wait for all threads to end.
    for downloadThread in downloadThreads:
        downloadThread.join()

    stop = timeit.default_timer()
    runTime = stop - start
    runTime = str(round(runTime, 2))

    print('Done downloading ' + str(comics) + ' XKCD comics with ' + str(threads) + ' threads.  Runtime is ' + runTime + ' seconds.')

for t in range(2, 13, 2):   # loop from 2 to 12 by 2's to get data on these number of threads
    manageThreads(comics=48, threads=t) # comics and threads