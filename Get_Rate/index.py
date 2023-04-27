import json
from tkinter import messagebox

import trafilatura
from bs4 import BeautifulSoup
from helper.index import *
from xpath_conf import sukma_convert


def get_rate_via_pulsa():
    downloaded = trafilatura.fetch_url('https://www.viapulsa.com/')
    soup = BeautifulSoup(downloaded, 'html.parser')
    element_rate = soup.find_all('p', class_='elementor-heading-title elementor-size-default')

    rate_dict = {"rate": []}

    for element in element_rate:
        rate_name = element.get_text(strip=True)
        rate_value = element.find_next('p').get_text(strip=True)
        rate_dict["rate"].append({rate_name: rate_value})

    json_cleaner(rate_dict)
    json_str = json.dumps(rate_dict)
    json_obj = json.loads(json_str)
    payload = {
        "company": "VIA PULSA",
        "rate": json_obj["rate"]
    }
    try:
        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from rate via pulsa")


def get_rate_by_pulsa():
    downloaded = trafilatura.fetch_url('https://bypulsa.com/')
    soup = BeautifulSoup(downloaded, 'html.parser')

    rate_dict = {"rate": []}
    rate_telkomsel(soup, rate_dict)
    rate_xl(soup, rate_dict)
    rate_Three(soup, rate_dict)
    rate_Indosat(soup, rate_dict)

    json_str = json.dumps(rate_dict)
    json_obj = json.loads(json_str)
    payload = {
        "company": "BY PULSA",
        "rate": json_obj["rate"]
    }

    try:
        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from rate via pulsa")


def get_rate_sukma_convert():
    url = 'https://www.sukmaconvert.com/'
    chrome_options = chrome_option()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)

    driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.35, behavior: 'smooth'});")
    time.sleep(3)

    convert_pulsa_xl_exis = sukma_convert["convert_pulsa_xl_exis"]
    convert_pulsa_xl_exis_text = driver.find_element(By.XPATH, convert_pulsa_xl_exis).text
    time.sleep(3)

    convert_pulsa_indoesat_mentari = sukma_convert["convert_pulsa_indoesat_mentari"]
    convert_pulsa_indoesat_mentari_text = driver.find_element(By.XPATH, convert_pulsa_indoesat_mentari).text
    time.sleep(3)

    convert_pulsa_telkomsel = sukma_convert["convert_pulsa_telkomsel"]
    convert_pulsa_telkomsel_text = driver.find_element(By.XPATH, convert_pulsa_telkomsel).text
    time.sleep(3)

    convert_pulsa_three = sukma_convert["convert_pulsa_three"]
    convert_pulsa_three_text = driver.find_element(By.XPATH, convert_pulsa_three).text
    time.sleep(3)

    rate_dict = {"rate": []}

    convert_pulsa_xl_exis_list = convert_pulsa_xl_exis_text.split('\n')
    rate_dict["rate"].append({"XL/Axis": convert_pulsa_xl_exis_list})

    convert_pulsa_indoesat_mentari_list = convert_pulsa_indoesat_mentari_text.split('\n')
    rate_dict["rate"].append({"Indosat/Mentari": convert_pulsa_indoesat_mentari_list})

    convert_pulsa_telkomsel_list = convert_pulsa_telkomsel_text.split('\n')
    rate_dict["rate"].append({"Telkomsel": convert_pulsa_telkomsel_list})

    convert_pulsa_three_list = convert_pulsa_three_text.split('\n')
    rate_dict["rate"].append({"Three": convert_pulsa_three_list})

    json_rate_dict = json.dumps(rate_dict)
    data = json.loads(json_rate_dict)
    rate_dict = {"company": "SUKMA CONVERT", "rate": []}

    for item in data["rate"]:
        for k, v in item.items():
            rate_dict["rate"].append({k: ' '.join(v[1:])})

    json_str = json.dumps(rate_dict)
    json_obj = json.loads(json_str)
    payload = {
        "company": "SUKMA CONVERT",
        "rate": json_obj["rate"]
    }

    try:
        url = 'https://ratepromo.vercel.app/rate'

        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from hit_rate_sukma_convert")

    driver.quit()


if __name__ == '__main__':
    get_rate_via_pulsa()
    get_rate_by_pulsa()
    get_rate_sukma_convert()
    messagebox.showinfo("Proses Selesai", "Proses telah selesai.")
