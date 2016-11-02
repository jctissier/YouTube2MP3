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

