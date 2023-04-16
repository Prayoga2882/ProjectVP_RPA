from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from lxml import html


def name_TSEL1():
    url = 'https://www.telkomsel.com/promo/DANA-cashback'
    text, soup = html_read_1(url)
    my_paragraph = soup.find('h1')
    if my_paragraph:
        text = my_paragraph.get_text()

    return text


def term_and_condition_TSEL1():
    url = 'https://www.telkomsel.com/promo/DANA-cashback'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    root = html.fromstring(str(soup))

    xpath_expression = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[2]/ol'
    li_element = root.xpath(xpath_expression)[0]
    li_text = li_element.text_content().strip()

    return li_text


def periode_TSEL1():
    url = 'https://www.telkomsel.com/promo/DANA-cashback'
    text, soup = html_read_1(url)

    my_paragraph = soup.find('div', {'class': 'left-promo-content'})
    if my_paragraph:
        text = my_paragraph.get_text()
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    # Mencari posisi angka pertama setelah 'PERIODEPROMO'
    posisi_angka_pertama = text.find('0')

    # Menyisipkan spasi antara 'PERIODE' dan 'PROMO'
    text = text[:posisi_angka_pertama] + ' ' + text[posisi_angka_pertama:]

    # Menyisipkan spasi antara tanggal dan bulan pada periode promo
    posisi_tanggal_akhir = text.find(' ', posisi_angka_pertama)
    posisi_bulan_awal = text.find('-', posisi_tanggal_akhir)
    posisi_bulan_akhir = text.find(' ', posisi_bulan_awal)
    text = text[:posisi_bulan_awal + 1] + ' ' + text[posisi_bulan_awal + 1:posisi_bulan_akhir] + ' ' + text[
                                                                                                       posisi_bulan_akhir:]

    # Mengganti tanda '–' dengan '-'
    text = text.replace('–', '-')

    return text


def html_read_1(url):
    html_parsing = urlopen(url).read()
    soup = BeautifulSoup(html_parsing, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text, soup
