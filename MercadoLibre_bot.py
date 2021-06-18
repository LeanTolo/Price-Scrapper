from selenium import webdriver
from time import sleep
from datetime import datetime as dt
from datetime import date

class Scraper:

    driver = webdriver.Chrome("C:/Users/Tolo/Desktop/Metod 2 Scrapper/Scrapper/Price-Scrapper/chromedriver.exe")

    def __init__(self, url):    
        self.url = url
        self.driver.get(self.url)
    
    def search(self, search):
        searcher = self.driver.find_element_by_xpath("/html/body/header/div/form/input")
        searcher.send_keys(search)
        search_button = self.driver.find_element_by_xpath("/html/body/header/div/form/button")
        search_button.click()
    
    def getInfo(self):
        objects = self.driver.find_elements_by_class_name("ui-search-layout__item")
        resultsSearch = {}
        for element in range(len(objects)):
            title = objects[element].find_element_by_class_name("ui-search-item__title").text
            price = objects[element].find_element_by_class_name("price-tag-fraction").text
            url = objects[element].find_element_by_css_selector(".ui-search-item__group__element.ui-search-link").get_attribute("href")

            if element not in resultsSearch:
                resultsSearch[element] = {
                    "title": title,
                    "price": price,
                    "URL": url
                }
        return resultsSearch

    def saveDataSearch(self, resultSearch):
        with open("data.txt", "w") as file:
            if dt.now().minute < 10:
                file.write(f"**SEARCH DATE: {date.today()} , {dt.now().hour}:0{dt.now().minute}hs **\n\n")
            else:
                file.write(f"**SEARCH DATE: {date.today()} , {dt.now().hour}:{dt.now().minute}hs**\n\n")
            for result in resultSearch:
                file.write(f"Result {result+1}:\n")
                file.write(f"--Title: {resultSearch[result]['title']}\n")
                file.write(f"--Price: ${resultSearch[result]['price']}\n")
                file.write(f"--URL: {resultSearch[result]['url']}\n\n\n")

    
x = Scraper("https://www.mercadolibre.com.ar/")
x.search("teclado")
data = x.getInfo()
