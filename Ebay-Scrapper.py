from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time


def main(search_term):
    driver = webdriver.Chrome()

    home_link = "https://www.ebay.com/"
    search_kw = search_term.replace(" ", "+")

    driver.get(
        home_link+"/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313&_nkw="+search_kw+"&_sacat=0")

    item_title = []
    item_link = []
    item_status = []
    item_score = []
    item_reviews_amt = []
    item_price = []

    pg_amount = 4

    page = BeautifulSoup(driver.page_source, 'html.parser')

    for i in range(0, pg_amount):
        for item in page.findAll('li', attrs={'class': 's-item', 'data-view': True}):
            title = item.find('h3', attrs={'class': 's-item__title'})
            if title:
                item_title.append(title.text)
            else:
                item_title.append('')

            link = item.find('a', attrs={'class': 's-item__link'})
            if link:
                item_link.append(link['href'])
            else:
                item_link.append('')

            status = item.find('div', attrs={'class': 's-item__subtitle'})
            if status:
                item_status.append(status.text)
            else:
                item_status.append('')

            score = item.find(
                'div', attrs={'class': ['b-starrating', 'x-star-rating']})
            if score:
                score.find('span', attrs={'class': 'clipped'})
                if score:
                    item_score.append(score.text[0:3])
                else:
                    item_score.append('')
            else:
                item_score.append('')

            reviews_amt = item.find(
                'span', attrs={'class': 's-item__reviews-count'})
            if reviews_amt:
                item_reviews_amt.append(
                    reviews_amt.span.text[0:reviews_amt.span.text.find('valor')-1])
            else:
                item_reviews_amt.append('')

            price = item.find('span', attrs={'class', 's-item__price'})
            if price:
                item_price.append(
                    float(''.join((price.text[4:(price.text+' a').find(' a')]).split())))
            else:
                item_price.append('')
        next_btn = driver.find_element_by_css_selector('.pagination__next')
        next_btn.click()
        time.sleep(2)

    item_list = pd.DataFrame({
        'TITLE': item_title,
        'STATUS': item_status,
        'SCORE': item_score,
        'REVIEWS_AMT': item_reviews_amt,
        'PRICE': item_price,
        'LINK': item_link
    })

    item_list = item_list.sort_values(
        by=['PRICE', 'SCORE', 'REVIEWS_AMT'], ascending=[True, False, False])


    item_list.to_csv(r'prueba.csv', index=None,
                     header=True, encoding='utf-8-sig')


main('rtx 3060')
