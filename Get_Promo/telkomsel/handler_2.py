from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from lxml import html


def name_TSEL2():
    url = 'https://www.telkomsel.com/promo/gopay-cashback-seluruh-pelanggan'
    text, soup = html_read_2(url)
    my_paragraph = soup.find('h1')
    if my_paragraph:
        text = my_paragraph.get_text()

    return text


def term_and_condition_TSEL2():
    url = 'https://www.telkomsel.com/promo/gopay-cashback-seluruh-pelanggan'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    root = html.fromstring(str(soup))

    xpath_expression = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[2]/ol'
    li_element = root.xpath(xpath_expression)[0]
    li_text = li_element.text_content().strip()

    return li_text


def periode_TSEL2():
    url = 'https://www.telkomsel.com/promo/gopay-cashback-seluruh-pelanggan'
    text, soup = html_read_2(url)

    my_paragraph = soup.find('div', {'class': 'left-promo-content'})
    if my_paragraph:
        text = my_paragraph.get_text()
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    string_setelah_1 = text.replace("\u2013", "-")

    string_setelah_2 = string_setelah_1[:12] + " " + string_setelah_1[12:17] + " " + string_setelah_1[
                                                                                     17:21] + " " + string_setelah_1[
                                                                                                    21:]

    string_setelah_3 = string_setelah_2[:28] + ":" + string_setelah_2[28:30] + string_setelah_2[30:]

    return string_setelah_3


def html_read_2(url):
    html_parsing = urlopen(url).read()
    soup = BeautifulSoup(html_parsing, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text, soup
