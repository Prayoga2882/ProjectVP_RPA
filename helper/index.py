import json
from selenium.webdriver.chrome.options import Options
import re
from datetime import datetime


def json_cleaner(rate_dict):
    indices_to_remove = [1, 3, 5, 7, 9, 11]
    indices_to_remove.sort(reverse=True)
    for index in indices_to_remove:
        if index < len(rate_dict['Rate']):
            rate_dict['Rate'].pop(index)


def rate_telkomsel(soup, rate_dict):
    class_element_telkomsel = 'elementor-element elementor-element-712e76c elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_telkomsel)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["Rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def rate_xl(soup, rate_dict):
    class_element_xl = 'elementor-element elementor-element-f4328c4 elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_xl)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["Rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def rate_Three(soup, rate_dict):
    class_element_Three = 'elementor-element elementor-element-8530d20 elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_Three)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["Rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def rate_Indosat(soup, rate_dict):
    class_element_Indosat = 'elementor-element elementor-element-0b048c0 elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_Indosat)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["Rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def chrome_option():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Menambahkan opsi headless
    chrome_options.add_argument("--disable-gpu")  # Menonaktifkan GPU
    chrome_options.add_argument("--disable-infobars")  # Menonaktifkan info bars
    chrome_options.add_argument("--disable-notifications")  # Menonaktifkan notifikasi
    chrome_options.add_argument("--window-size=1920x1080")  # Mengatur ukuran jendela
    chrome_options.add_argument("--disable-extensions")  # Menonaktifkan ekstensi
    chrome_options.add_argument("--disable-dev-shm-usage")  # Menonaktifkan penggunaan /dev/shm
    chrome_options.add_argument("--no-sandbox")  # Menonaktifkan mode sandbox
    return chrome_options


def format_periode(data):
    # data = "01April-20April2023(00.00–23.59WIB)"
    tanggal_awal = re.findall(r"\d{2}[A-Za-z]+", data)[0]
    tanggal_akhir = re.findall(r"\d{2}[A-Za-z]+\d{4}", data)
    tahun_sekarang = datetime.now().year

    if tanggal_akhir:
        tanggal_akhir = tanggal_akhir[0]
        tanggal_akhir = datetime.strptime(tanggal_akhir, '%d%B%Y').replace(year=tahun_sekarang).strftime('%Y-%m-%d')
    else:
        tanggal_akhir = None

    tanggal_awal = datetime.strptime(tanggal_awal, '%d%B').replace(year=tahun_sekarang).strftime('%Y-%m-%d')

    json_data = {
        "startDate": tanggal_awal,
        "endDate": tanggal_akhir
    }
    start_date = json_data['startDate']
    end_date = json_data['endDate']

    return start_date, end_date

