import requests
import pandas as pd


url = 'http://api.instagram.com'

retorno = requests.get(url)

print (retorno)


