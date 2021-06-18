from selenium import webdriver
from time import sleep
from datetime import datetime as dt
from datetime import date
import pandas as pd
    

class MeliBot(object):
    def main(search_term):
        driver = webdriver.Chrome("C:/Users/Tolo/Desktop/Metod 2 Scrapper/Scrapper/Price-Scrapper/chromedriver.exe")
        driver.get("https://www.mercadolibre.com.ar/")

        searcher = driver.find_element_by_xpath("/html/body/header/div/form/input")
        searcher.send_keys(search_term)
        search_button = driver.find_element_by_xpath("/html/body/header/div/form/button")
        search_button.click()
        
        objects = driver.find_elements_by_class_name("ui-search-layout__item")

        item_title = []
        item_price = []
        item_link = []

        for element in range(len(objects)):
            title = objects[element].find_element_by_class_name("ui-search-item__title").text
            price = objects[element].find_element_by_class_name("price-tag-fraction").text
            url = objects[element].find_element_by_css_selector(".ui-search-item__group__element.ui-search-link").get_attribute("href")
            item_title.append(title)  
            item_price.append(price)
            item_link.append(url)

        driver.close()

        item_list = pd.DataFrame({
            'TITLE': item_title,
            'PRICE': item_price,
            'URL': item_link
        })
        item_list.drop_duplicates().to_csv(r'MercadoLibre.csv', index=None,
                        header=True, encoding='utf-8-sig')

