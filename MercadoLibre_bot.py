from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


import re
import time



class MercadoLibreBot(object):
    def __init__(self, items):
        self.mercadolibre_url = "https://www.mercadolibre.com.ar/"
        self.items = items

        self.driver = webdriver.Chrome("C:/Users/Tolo/Desktop/Metod 2 Scrapper/Scrapper/Price-Scrapper/chromedriver.exe")
        self.driver.get(self.mercadolibre_url)

    def search_items(self):
        urls = []
        precios = []
        nombres = []
        for item in self.items:
            print(f"Buscando...{item}")
            self.driver.get(self.mercadolibre_url)
            search_input = self.driver.find_element_by_class_name("nav-search-input")
            search_input.send_keys(item)
            time.sleep(2)
            search_button = self.driver.find_element_by_xpath("/html/body/header/div/form/button/div")
            search_button.click()
            time.sleep(2)
            first_result = self.driver.find_element_by_xpath("/html/body/main/div[1]/div/section/ol/li[1]/div/div[1]/div/a")
            url = first_result.get_attribute("href")

            precio = self.get_product_price(url)
            nombre = self.get_product_name(url)

            precios.append(precio)
            urls.append(url)
            nombres.append(nombre)
            print(nombre)
            print(precio)
            print(url)
            time.sleep(2)
        return precios, urls, nombres

    def get_product_price(self, url):
        self.driver.get(url)
        try:
            precio = self.driver.find_element_by_class_name("price-tag-fraction").text
        except:
            pass

        if precio is None:
            precio = "NO VALIDO"


        return precio

    def get_product_name(self, url):
        self.driver.get(url)
        try:
            product_name = self.driver.find_element_by_class_name("ui-pdp-title").text
        except:
            pass
        if product_name is None:
            product_name = "NO VALIDO"
        return product_name

