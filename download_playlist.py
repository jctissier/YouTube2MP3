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
