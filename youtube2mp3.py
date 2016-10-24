import webbrowser
from termcolor import cprint, colored
import requests
import warnings
from bs4 import BeautifulSoup
from pprint import pprint
import time

choose = colored("Paste your link and click ENTER:\n", 'red')
link = input(choose)

main_link = 'http://www.youtubeinmp3.com'
mp3_download_link = 'http://www.youtubeinmp3.com/download/?video='
mp3_download_info = 'http://www.youtubeinmp3.com/fetch/?format=JSON&bitrate=1&filesize=1&video='
extension = '&autostart=1'

# Get the link and open it
full_link = mp3_download_link + link
r = requests.get(full_link)
soup = BeautifulSoup(r.content, "lxml")
href = soup.find_all("a", {"id": "download"})
href_link = href[0].get('href')
webbrowser.open_new_tab(main_link + href_link)
