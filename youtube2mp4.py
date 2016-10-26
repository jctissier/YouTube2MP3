import webbrowser
from termcolor import cprint, colored
import requests
import warnings
from bs4 import BeautifulSoup
import time

# Request user input
choose = colored("Paste your link and click ENTER:\n", 'red')
link = input(choose)
