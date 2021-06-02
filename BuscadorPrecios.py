from MercadoLibre_bot import MercadoLibreBot
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}



class PriceUpdater(object):

    def process_items_list(self):
        items = ['iphone 11', 'licuadora']
        print(" Articulos para buscar....")
        MercadoLibre_bot = MercadoLibreBot(items)
        precios, urls, nombres = MercadoLibre_bot.search_items()


price_updater = PriceUpdater()
price_updater.process_items_list()







