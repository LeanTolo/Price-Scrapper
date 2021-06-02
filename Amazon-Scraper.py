## BLOCK
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

##URL
def get_url(search_term):
    template = 'https://www.amazon.com/s?k={}'
    search_term = search_term.replace(' ', '+')
    
    # Add Term Query To URL
    url = template.format(search_term)
    
    # Add Page Query Placeholder
    url += '&page={}'
    
    return url


##RECORD
def extract_record(item):
    ##Description and URL
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')
    
    #Price
    try:
        price_parent = item.find('span','a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return
    #Rank and Rating
    try:
        rating = item.i.text
        review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        rating = ''
        review_count = ''
    
    result = (description, price, rating, review_count, url)
    return result

##MAIN
def main(search_term):
    ##inicializamos el webdriver
    driver = webdriver.Chrome()

    records = []
    url = get_url(search_term)

    ##va de la pagina 1 al 20
    for page in range (1,4):
        driver.get(url.format(page))
        soup =BeautifulSoup(driver.page_source, 'html.parser')

        results = soup.find_all('div',{'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    
    driver.close()

    ##Guardar la data en csv comas, separated values
    with open('amazon.csv','w',newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price', 'Rating', 'Reviews', 'Url'])
        writer.writerows(records)

main('xiaomi')