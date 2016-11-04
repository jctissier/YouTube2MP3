import webbrowser
from termcolor import cprint, colored
import requests
import warnings
from bs4 import BeautifulSoup
from pprint import pprint
import time

# Globals
main_link = 'http://www.youtube.com'
mp3_download_link = 'http://www.youtubeinmp3.com/download/?video='
mp3_download_info = 'http://www.youtubeinmp3.com/fetch/?format=JSON&bitrate=1&filesize=1&video='
extension = '&autostart=1'

def main():
    r = requests.get(playlist_link)
    soup = BeautifulSoup(r.content, "lxml")
    if "list" in playlist_link:
        print("Request to download whole list")
        download_playlist_info(soup)
    else:
        print("Go to single download")
        
def download_playlist_info(soup):
    try:
        # Playlist info
        length = soup.find_all("span", {"id": "playlist-length"})[0]                   # Get playlist length
        list_length = int(length.text.replace("videos", ""))
        print("{:<20}{:<20}".format("Playlist Length: ", colored(str(list_length) + " videos",'red')))
        title = soup.find_all("h3", {"class": "playlist-title"})[0].text
        print("{:<20}{:<20}".format('Playlist Title: ', colored(title.strip(),'red')))
        author = soup.find_all("li", {"class": "author-attribution"})[0].text
        print("{:<20}{:<20}".format('Playlist Author: ', colored(author.strip(),'red')))
        download_playlist(soup, start=0, playlist_size=list_length)
    except IndexError:
        print("This is not a playlist, redirect to method that downloads one song")

        
def download_playlist(soup, start, playlist_size):
        try:
            for x in range(start, playlist_size):
                href = soup.find_all("a", {"class": "yt-uix-sessionlink spf-link playlist-video clearfix spf-link "})[x]
                # print(href.get('href'))
                song_info(href_string=href, index=x)
                download_songs(href_string=href)
        except IndexError:
            print("Video #" + str(x+1) + " in the playlist has been removed or is not valid...")
            download_playlist(soup, start=x+1, playlist_size=playlist_size)

def song_info(href_string, index):
    # JSON parser to get media info
    r = requests.get(mp3_download_info + str(href_string))
    data = r.json()
    title = data['title']
    length = time.strftime("%M:%S", time.gmtime(int(data['length'])))
    file_size = int(data['filesize']) / 1000000
    bitrate = data['bitrate']
    
    cprint("\nDownloading Song: #" + str(index + 1), 'yellow')
    print("{:<20}".format("Title:") + colored(title, 'blue'))
    print("{:<20}".format("Length:") + colored(length, 'blue'))
    print("{:<20}".format("Size:") + colored("{0:.1f}".format(file_size) + "MB", 'blue'))
    print("{:<20}".format("Bitrate:") + colored(bitrate + "kbps", 'blue'))
    if index == 0:
        pass
    elif index == 10 or index == 20 or index == 30 or index == 40:
        time.sleep(10)
    else:
        time.sleep(3)
        
def download_songs(href_string):
    full_link = mp3_download_link + str(href_string)
    r = requests.get(full_link)
    soup = BeautifulSoup(r.content, "lxml")
    href = soup.find_all("a", {"id": "download"})
    href_link = href[0].get('href')
    print(main_link + href_link)



    
    
