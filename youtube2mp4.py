import webbrowser
from termcolor import cprint, colored
import requests
import warnings
from bs4 import BeautifulSoup
import time

# Request user input
choose = colored("Paste your link and click ENTER:\n", 'red')
link = input(choose)
mp4_download_link = 'http://www.youtubeinmp4.com/youtube.php?video='
mp4_link = 'http://www.youtubeinmp4.com/'
mp4_link = 'http://www.youtubeinmp4.com/'
r = requests.get(full_link)
soup = BeautifulSoup(r.content, "lxml")
href = soup.find_all("a", {"id": "downloadMP4"})
href_link = href[1].get('href')
