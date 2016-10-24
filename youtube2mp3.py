import webbrowser
from termcolor import cprint, colored
import requests
import warnings
from bs4 import BeautifulSoup
from pprint import pprint
import time

choose = colored("Paste your link and click ENTER:\n", 'red')
link = input(choose)
