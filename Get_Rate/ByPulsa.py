import json
import trafilatura
from bs4 import BeautifulSoup
from helper.index import *


def get_rate_via_pulsa():
    downloaded = trafilatura.fetch_url('https://www.viapulsa.com/')
    soup = BeautifulSoup(downloaded, 'html.parser')
    element_rate = soup.find_all('p', class_='elementor-heading-title elementor-size-default')

    rate_dict = {"Rate": []}

    for element in element_rate:
        rate_name = element.get_text(strip=True)
        rate_value = element.find_next('p').get_text(strip=True)
        rate_dict["Rate"].append({rate_name: rate_value})

    json_cleaner(rate_dict)
    result = json.dumps(rate_dict)
    print(result)


def get_rate_by_pulsa():
    downloaded = trafilatura.fetch_url('https://bypulsa.com/')
    soup = BeautifulSoup(downloaded, 'html.parser')

    rate_dict = {"Rate": []}
    rate_telkomsel(soup, rate_dict)
    rate_xl(soup, rate_dict)
    rate_Three(soup, rate_dict)
    rate_Indosat(soup, rate_dict)

    result = json.dumps(rate_dict)
    print(result)


if __name__ == '__main__':
    # get_rate_via_pulsa()
    get_rate_by_pulsa()
