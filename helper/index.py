import time

import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
import trafilatura
import requests
import re
import json
from datetime import timedelta
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import dateutil.parser
import datetime as dt


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


def json_cleaner(rate_dict):
    indices_to_remove = [1, 3, 5, 7, 9, 11]
    indices_to_remove.sort(reverse=True)
    for index in indices_to_remove:
        if index < len(rate_dict['rate']):
            rate_dict['rate'].pop(index)


def rate_telkomsel(soup, rate_dict):
    class_element_telkomsel = 'elementor-element elementor-element-712e76c elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_telkomsel)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def rate_xl(soup, rate_dict):
    class_element_xl = 'elementor-element elementor-element-f4328c4 elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_xl)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def rate_Three(soup, rate_dict):
    class_element_Three = 'elementor-element elementor-element-8530d20 elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_Three)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def rate_Indosat(soup, rate_dict):
    class_element_Indosat = 'elementor-element elementor-element-0b048c0 elementor-widget elementor-widget-iprogress'
    element_rate = soup.find_all('div', class_=class_element_Indosat)

    for element in element_rate:
        rate_name = element.find('span', class_='pname fleft').get_text(strip=True)
        rate_value = element.find('span', class_='ppercent fright').get_text(strip=True)
        rate_dict["rate"].append({rate_name: rate_value})

    result = json.dumps(rate_dict)
    return result


def rate_telkomsel_zahra_convert(driver):
    try:
        rate = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[1]"
        rate = driver.find_element(By.XPATH, rate).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate})

        new_data = {'company': 'ZAHRA CONVERT', 'rate': []}

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                new_data['rate'].append(rate_item)

        new_data = json.dumps(new_data)
        new_data = json.loads(new_data)
        return new_data['rate']
    except Exception as e:
        print("Error from rate_telkomsel_zahra_convert: ", e)


def rate_tri_zahra_convert(driver):
    try:
        rate = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[2]"
        rate = driver.find_element(By.XPATH, rate).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate})

        new_data = {'company': 'ZAHRA CONVERT', 'rate': []}

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                new_data['rate'].append(rate_item)

        new_data = json.dumps(new_data)
        print("rate_tri_zahra_convert: ", new_data)
        return new_data
    except Exception as e:
        print("Error from rate_tri_zahra_convert: ", e)


def rate_indosat_zahra_convert(driver):
    try:
        rate = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[3]"
        rate = driver.find_element(By.XPATH, rate).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate})

        new_data = {'company': 'ZAHRA CONVERT', 'rate': []}

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                new_data['rate'].append(rate_item)

        new_data = json.dumps(new_data)
        print("rate_indosat_zahra_convert: ", new_data)
        return new_data
    except Exception as e:
        print("Error from rate_indosat_zahra_convert: ", e)


def rate_xl_axis_zahra_convert(driver):
    try:
        rate = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[4]"
        rate = driver.find_element(By.XPATH, rate).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate})

        new_data = {'company': 'ZAHRA CONVERT', 'rate': []}

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                new_data['rate'].append(rate_item)

        new_data = json.dumps(new_data)
        print("rate_xl_axis_zahra_convert: ", new_data)
        return new_data
    except Exception as e:
        print("Error from rate_xl_axis_zahra_convert: ", e)


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


def clean_promo_tokopedia(lines):
    # ambil tanggal dan bulan
    date_range = lines[2].split("-")
    start_date_str = date_range[0].strip()
    end_date_str = date_range[1].strip()

    # ubah format bulan menjadi angka
    months = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'Mei': '05',
        'Jun': '06',
        'Jul': '07',
        'Ags': '08',
        'Sep': '09',
        'Okt': '10',
        'Nov': '11',
        'Des': '12'
    }

    start_date_parts = start_date_str.split(" ")
    start_month = months[start_date_parts[1]]
    start_day = start_date_parts[0]
    start_date = datetime.strptime(f"2023-{start_month}-{start_day}", '%Y-%m-%d').date()

    end_date_parts = end_date_str.split(" ")
    end_month = months[end_date_parts[1]]
    end_day = end_date_parts[0]
    end_date = datetime.strptime(f"2023-{end_month}-{end_day}", '%Y-%m-%d').date()

    return start_date, end_date


def clean_promo_shopee(driver, promo):
    text_promo = driver.find_element(By.XPATH, promo).text
    details = {
        "name": "",
        "periode": "",
        "detail": ""
    }

    lines = text_promo.split('\n')
    details["name"] = lines[0]
    details["periode"] = lines[1]
    details["detail"] = lines[2]
    details.pop("detail", None)
    date_str = details["periode"].replace("Berlaku Hingga: ", "")
    date_obj = datetime.strptime(date_str, '%d-%m-%Y')
    details["periode"] = date_obj.strftime('%Y-%m-%d')

    return details


def format_periode(data):
    # data = '18 April - 30 April 2023'
    date_range, year = data.rsplit(" ", 1)
    start_date_str, end_date_str = date_range.split(" - ")

    output = {
        "startDate": f"{year.strip()}-{get_month_number(start_date_str.split()[1])}-{start_date_str.split()[0]}",
        "endDate": f"{year.strip()}-{get_month_number(end_date_str.split()[1])}-{end_date_str.split()[0]}"
    }
    return output


def generate_promo_telkomsel():
    downloaded = trafilatura.fetch_url('https://www.telkomsel.com/promo')
    soup = BeautifulSoup(downloaded, 'html.parser')
    element_rate = soup.find_all('div', class_='promo-name')
    # name
    name = []
    for i in element_rate:
        if i.text != '':
            name.append(i.text)

    hit_promoTSEL1(name)
    hit_promoTSEL2(name)
    hit_promoTSEL3(name)
    hit_promoTSEL4(name)
    hit_promoTSEL5(name)
    hit_promoTSEL6(name)

    print("Success", "Promo Telkomsel has been generated!")


def hit_promoTSEL1(name):
    try:
        url = "https://www.telkomsel.com/promo"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        cookes = '//*[@id="cookiesSection"]/div/div/div/div/div[2]/button'
        driver.find_element(By.XPATH, cookes).click()
        time.sleep(3)
        scroll_25(driver)

        promo1 = '/html/body/div[5]/div[2]/div/div/section/div/div/div/div/a[1]/div/div/div[2]'
        driver.find_element(By.XPATH, promo1).click()
        time.sleep(3)
        scroll_25(driver)

        result_tnc = driver.find_element(By.CLASS_NAME, "typografi-g-body-1-bold").text
        periode = format_periode(result_tnc)
        scroll_25(driver)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "telkomsel",
            "name": name[0],
            "url": url_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_telkomsel 1: ", e)


def hit_promoTSEL2(name):
    try:
        url = "https://www.telkomsel.com/promo"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        cookes = '//*[@id="cookiesSection"]/div/div/div/div/div[2]/button'
        driver.find_element(By.XPATH, cookes).click()
        time.sleep(3)
        scroll_25(driver)

        promo2 = '/html/body/div[5]/div[2]/div/div/section/div/div/div/div/a[2]/div/div/div[2]/div[2]'
        driver.find_element(By.XPATH, promo2).click()
        time.sleep(3)
        scroll_25(driver)

        result_tnc = driver.find_element(By.CLASS_NAME, "typografi-g-body-1-bold").text
        periode = format_periode(result_tnc)
        scroll_25(driver)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "telkomsel",
            "name": name[1],
            "url": url_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_telkomsel 2: ", e)


def hit_promoTSEL3(name):
    try:
        url = "https://www.telkomsel.com/promo"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        cookes = '//*[@id="cookiesSection"]/div/div/div/div/div[2]/button'
        driver.find_element(By.XPATH, cookes).click()
        time.sleep(3)
        scroll_25(driver)

        promo3 = '/html/body/div[5]/div[2]/div/div/section/div/div/div/div/a[3]/div/div/div[2]/div[2]'
        driver.find_element(By.XPATH, promo3).click()
        time.sleep(3)
        scroll_25(driver)

        result_tnc = driver.find_element(By.CLASS_NAME, "typografi-g-body-1-bold").text
        periode = format_periode(result_tnc)
        scroll_25(driver)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "telkomsel",
            "name": name[2],
            "url": url_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_telkomsel 3: ", e)


def hit_promoTSEL4(name):
    try:
        url = "https://www.telkomsel.com/promo"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        cookes = '//*[@id="cookiesSection"]/div/div/div/div/div[2]/button'
        driver.find_element(By.XPATH, cookes).click()
        time.sleep(3)
        scroll_25(driver)

        promo4 = '/html/body/div[5]/div[2]/div/div/section/div/div/div/div/a[4]/div/div/div[2]/div[2]'
        driver.find_element(By.XPATH, promo4).click()
        time.sleep(3)
        scroll_25(driver)

        result_tnc = driver.find_element(By.CLASS_NAME, "typografi-g-body-1-bold").text
        periode = format_periode(result_tnc)
        scroll_25(driver)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "telkomsel",
            "name": name[3],
            "url": url_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_telkomsel 4: ", e)


def hit_promoTSEL5(name):
    try:
        url = "https://www.telkomsel.com/promo"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        cookes = '//*[@id="cookiesSection"]/div/div/div/div/div[2]/button'
        driver.find_element(By.XPATH, cookes).click()
        time.sleep(3)
        scroll_25(driver)

        promo5 = '/html/body/div[5]/div[2]/div/div/section/div/div/div/div/a[5]/div/div/div[2]/div[2]'
        driver.find_element(By.XPATH, promo5).click()
        time.sleep(3)
        scroll_25(driver)

        result_tnc = driver.find_element(By.CLASS_NAME, "typografi-g-body-1-bold").text
        periode = format_periode(result_tnc)
        scroll_25(driver)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "telkomsel",
            "name": name[4],
            "url": url_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_telkomsel 5: ", e)


def hit_promoTSEL6(name):
    try:
        url = "https://www.telkomsel.com/promo"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        cookes = '//*[@id="cookiesSection"]/div/div/div/div/div[2]/button'
        driver.find_element(By.XPATH, cookes).click()
        time.sleep(3)
        scroll_25(driver)

        promo6 = '/html/body/div[5]/div[2]/div/div/section/div/div/div/div/a[6]/div/div/div[2]/div[2]'
        driver.find_element(By.XPATH, promo6).click()
        time.sleep(3)
        scroll_25(driver)

        result_tnc = driver.find_element(By.CLASS_NAME, "typografi-g-body-1-bold").text
        periode = format_periode(result_tnc)
        scroll_25(driver)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "telkomsel",
            "name": name[5],
            "url": url_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_telkomsel 6: ", e)


def scroll_25(driver):
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.25, behavior: 'smooth'});")
    time.sleep(3)


def get_month_number(month):
    months = {
        'Januari': '01',
        'Februari': '02',
        'Maret': '03',
        'April': '04',
        'Mei': '05',
        'Juni': '06',
        'Juli': '07',
        'Agustus': '08',
        'September': '09',
        'Oktober': '10',
        'November': '11',
        'Desember': '12'
    }
    return months[month]


def get_promo_tokopedia():
    try:
        url = 'https://www.tokopedia.com/promo/'
        # chrome_options = chrome_option()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.33, behavior: 'smooth'});")
        time.sleep(3)

        hit_promo_tokped1(driver)
        hit_promo_tokped2(driver)
        hit_promo_tokped3(driver)
        hit_promo_tokped4(driver)

        print("Info", "Success Hit Promo Tokopedia")

    except Exception as e:
        print("Error from get_promo_tokopedia: ", e)


def hit_promo_tokped1(driver):
    try:
        promo1 = '/html/body/main/div[2]/section[3]/div/div[1]'
        prom1_text = driver.find_element(By.XPATH, promo1).text
        lines = prom1_text.split("\n")

        statDate, endDate = clean_promo_tokopedia(lines)

        url = 'https://ratepromo.vercel.app/promo'
        url_tnc = driver.current_url

        payload = {
            "provider": "Tokopedia",
            "name": lines[0],
            "url": url_tnc,
            "startDate": str(statDate),
            "endDate": str(endDate),
            "isActive": 1

        }
        json_data = json.dumps(payload)
        payload = json.loads(json_data)
        print("payload: ", payload)

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())

    except Exception as e:
        print("Error from hit_promo_tokped 1: ", e)


def hit_promo_tokped2(driver):
    try:
        promo2 = '/html/body/main/div[2]/section[3]/div/div[2]'
        promo2_text = driver.find_element(By.XPATH, promo2).text
        lines = promo2_text.split("\n")

        statDate, endDate = clean_promo_tokopedia(lines)

        url = 'https://ratepromo.vercel.app/promo'
        url_tnc = driver.current_url

        payload = {
            "provider": "Tokopedia",
            "name": lines[0],
            "url": url_tnc,
            "startDate": str(statDate),
            "endDate": str(endDate),
            "isActive": 1

        }
        json_data = json.dumps(payload)
        payload = json.loads(json_data)
        print("payload: ", payload)

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())

    except Exception as e:
        print("Error from hit_promo_tokped 2: ", e)


def hit_promo_tokped3(driver):
    try:
        promo3 = '/html/body/main/div[2]/section[3]/div/div[3]'
        promo3_text = driver.find_element(By.XPATH, promo3).text
        lines = promo3_text.split("\n")

        statDate, endDate = clean_promo_tokopedia(lines)

        url = 'https://ratepromo.vercel.app/promo'
        url_tnc = driver.current_url

        payload = {
            "provider": "Tokopedia",
            "name": lines[0],
            "url": url_tnc,
            "startDate": str(statDate),
            "endDate": str(endDate),
            "isActive": 1

        }
        json_data = json.dumps(payload)
        payload = json.loads(json_data)
        print("payload: ", payload)

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_tokped 3: ", e)


def hit_promo_tokped4(driver):
    try:
        promo4 = '/html/body/main/div[2]/section[3]/div/div[4]'
        promo4_text = driver.find_element(By.XPATH, promo4).text
        lines = promo4_text.split("\n")

        statDate, endDate = clean_promo_tokopedia(lines)

        url = 'https://ratepromo.vercel.app/promo'
        url_tnc = driver.current_url

        payload = {
            "provider": "Tokopedia",
            "name": lines[0],
            "url": url_tnc,
            "startDate": str(statDate),
            "endDate": str(endDate),
            "isActive": 1

        }
        json_data = json.dumps(payload)
        payload = json.loads(json_data)
        print("payload: ", payload)

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_tokped 4: ", e)


def get_promo_shopee():
    url = 'https://shopee.co.id/campaigns'
    chrome_options = chrome_option()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)

    driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.10, behavior: 'smooth'});")

    hit_promo_shopee1(driver)
    hit_promo_shopee2(driver)
    hit_promo_shopee3(driver)
    hit_promo_shopee4(driver)
    hit_promo_shopee5(driver)
    hit_promo_shopee6(driver)
    hit_promo_shopee7(driver)
    hit_promo_shopee8(driver)
    hit_promo_shopee9(driver)

    print("Selesai", "Generate Promo Shopee Selesai")


def hit_promo_shopee1(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 1: ", e)


def hit_promo_shopee2(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 2: ", e)


def hit_promo_shopee3(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[3]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 3: ", e)


def hit_promo_shopee4(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[4]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 4: ", e)


def hit_promo_shopee5(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 5: ", e)


def hit_promo_shopee6(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[6]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 6: ", e)


def hit_promo_shopee7(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[7]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 7: ", e)


def hit_promo_shopee8(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[8]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 8: ", e)


def hit_promo_shopee9(driver):
    try:
        promo = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[9]'
        details = clean_promo_shopee(driver, promo)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "Shopee",
            "name": details["name"],
            "url": url_tnc,
            "startDate": datetime.now().strftime('%Y-%m-%d'),
            "endDate": details["periode"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_shopee 9: ", e)


def generate_promo_axis():
    hit_promoAXIS1()
    # hit_promoAXIS2()

    print("Success", "Promo Axis has been generated!")


def hit_promoAXIS1():
    try:
        url = 'https://www.axis.co.id/promo'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)
        check = driver.find_element(By.XPATH, '//*[@id="modal-package-access"]/div/div/button/i')
        if check:
            check.click()
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.40, behavior: 'smooth'});")
        time.sleep(3)

        step1 = '/html/body/section[1]/div/div[3]/div/div[1]/a/div[1]/img'
        driver.find_element(By.XPATH, step1).click()
        time.sleep(3)

        step2 = '/html/body/section[1]/div/div/div/div[1]/h1'
        name = driver.find_element(By.XPATH, step2).text
        time.sleep(3)

        step3 = '/html/body/section[1]/div/div/div/div[2]/p[1]'
        periode = driver.find_element(By.XPATH, step3).text
        result_periode = periode_format_axis(periode)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "axis",
            "name": name,
            "url": url_tnc,
            "startDate": result_periode["startDate"],
            "endDate": result_periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_axis 1: ", e)


def hit_promoAXIS2():
    try:
        url = 'https://www.axis.co.id/promo'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)
        check = driver.find_element(By.XPATH, '//*[@id="modal-package-access"]/div/div/button/i')
        if check:
            check.click()
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.40, behavior: 'smooth'});")
        time.sleep(3)

        step1 = '/html/body/section[1]/div/div[3]/div/div[2]/a/div[1]/img'
        driver.find_element(By.XPATH, step1).click()
        time.sleep(3)

        step2 = '/html/body/section[1]/div/div/div/div[1]/h1'
        name = driver.find_element(By.XPATH, step2).text
        time.sleep(3)

        step3 = '/html/body/section[1]/div/div/div/div[2]/p[2]'
        periode = driver.find_element(By.XPATH, step3).text
        print("periode  :", periode)

        url_tnc = driver.current_url

        url = 'https://ratepromo.vercel.app/promo'
        # payload = {
        #     "provider": "axis",
        #     "name": name,
        #     "url": url_tnc,
        #     "startDate": result_periode["startDate"],
        #     "endDate": result_periode["endDate"],
        #     "isActive": 1
        # }

        # response = requests.post(url, json=payload)
        # requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        # print('Status Code:', response.status_code)
        # print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_axis 2: ", e)


def XL_core():
    url = 'https://www.xl.co.id/mobile/prabayar/promo-detail'
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)

    driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.30, behavior: 'smooth'});")
    time.sleep(3)
    step1 = '/html/body/div[1]/main/div/div[2]/div/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/img'
    driver.find_element(By.XPATH, step1).click()
    time.sleep(3)

    step2 = '/html/body/div[1]/main/div[1]/div[2]/div/h1'
    name = driver.find_element(By.XPATH, step2).text
    print(name)


def periode_format_axis(data):
    # data = "Periode Program: 16 Maret – 15 Mei 2023"
    data = data.replace("Periode Program: ", "")

    bulan = {'Januari': '01', 'Februari': '02', 'Maret': '03', 'April': '04', 'Mei': '05', 'Juni': '06',
             'Juli': '07', 'Agustus': '08', 'September': '09', 'Oktober': '10', 'November': '11', 'Desember': '12'}

    for nama_bulan, angka_bulan in bulan.items():
        data = data.replace(nama_bulan, angka_bulan)

    data = data.replace('-', ' ')
    data = data.replace("–", "-")
    tanggal_awal, tanggal_akhir = data.split(" - ")

    parsed_tanggal_awal = dateutil.parser.parse(tanggal_awal, dayfirst=True)
    parsed_tanggal_akhir = dateutil.parser.parse(tanggal_akhir, dayfirst=True)

    json_result = {
        "startDate": parsed_tanggal_awal.strftime("%Y-%m-%d"),
        "endDate": parsed_tanggal_akhir.strftime("%Y-%m-%d")
    }

    return json_result


def generate_promo_indosat():
    hit_promo_isat1()
    hit_promo_isat2()
    hit_promo_isat3()

    print("Info", "Generate Promo Indosat Berhasil")


def hit_promo_isat1():
    try:
        url = "https://indosatooredoo.com/portal/id/pspromolanding"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        step1 = '/html/body/div[1]/section[2]/div/div/div[2]/div/section[1]/div[1]/h4'
        name = driver.find_element(By.XPATH, step1).text
        time.sleep(3)

        step2 = '/html/body/div[1]/section[2]/div/div/div[2]/div/section[1]/div[2]/div/div/div[3]/a/span'
        driver.find_element(By.XPATH, step2).click()
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.50, behavior: 'smooth'});")
        time.sleep(3)

        url_tnc = driver.current_url

        step3 = '/html/body/div[1]/div[4]/section[3]/div/div[2]/div/div/div/div[2]/div[1]/a'
        driver.find_element(By.XPATH, step3).click()
        time.sleep(3)

        step4 = '/html/body/div[1]/div[4]/section[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div'
        periode = driver.find_element(By.XPATH, step4).text
        time.sleep(3)

        tanggal = re.search(r'Tanggal (\d+)', periode).group(1)
        start_date = datetime.strptime(tanggal, '%d')
        start_date = start_date.replace(year=2022, month=12)
        end_date = start_date + timedelta(days=9)

        json_data = {
            "startDate": start_date.strftime('%Y-%m-%d'),
            "endDate": end_date.strftime('%Y-%m-%d')
        }

        jadwal = json.dumps(json_data)
        jadwal = json.loads(jadwal)

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "indosat",
            "name": name,
            "url": url_tnc,
            "startDate": jadwal["startDate"],
            "endDate": jadwal["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_indosat 1: ", e)


def hit_promo_isat2():
    try:
        url = "https://www.indosatooredoo.com/portal/id/pspromo_inboundroaming"
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        step1 = '/html/body/div[1]/div[4]/div/div/div/h3'
        name = driver.find_element(By.XPATH, step1).text
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.20, behavior: 'smooth'});")
        time.sleep(3)
        url_tnc = driver.current_url

        step4 = '/html/body/div[1]/div[4]/div/div/div/p[2]'
        periode = driver.find_element(By.XPATH, step4).text
        time.sleep(3)

        tanggal = re.findall(r'\d{1,2} \w+', periode)

        bulan_dict = {
            'Januari': 'January',
            'Februari': 'February',
            'Maret': 'March',
            'April': 'April',
            'Mei': 'May',
            'Juni': 'June',
            'Juli': 'July',
            'Agustus': 'August',
            'September': 'September',
            'Oktober': 'October',
            'November': 'November',
            'Desember': 'December'
        }
        start_date_str = tanggal[0].split()
        start_date_str[1] = bulan_dict[start_date_str[1]]
        start_date_str.append('2021')
        start_date = datetime.strptime(' '.join(start_date_str), '%d %B %Y')
        end_date_str = tanggal[1].split()
        end_date_str[1] = bulan_dict[end_date_str[1]]
        end_date_str.append('2021')
        end_date = datetime.strptime(' '.join(end_date_str), '%d %B %Y')

        json_data = {
            "startDate": start_date.strftime('%Y-%m-%d'),
            "endDate": end_date.strftime('%Y-%m-%d')
        }

        jadwal = json.dumps(json_data)
        jadwal = json.loads(jadwal)

        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "indosat",
            "name": name,
            "url": url_tnc,
            "startDate": jadwal["startDate"],
            "endDate": jadwal["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())

    except Exception as e:
        print("Error from hit_promo_indosat 2: ", e)


def hit_promo_isat3():
    try:
        url = 'https://indosatooredoo.com/portal/id/psdevicebundle'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        step1 = '/html/body/div[1]/div[4]/section[1]/div/div/h3'
        name = driver.find_element(By.XPATH, step1).text
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.80, behavior: 'smooth'});")
        time.sleep(3)
        url_tnc = driver.current_url

        step2 = '/html/body/div[1]/div[4]/section[4]/div/div[2]/div/div/div/div[2]/div[1]/a'
        driver.find_element(By.XPATH, step2).click()
        time.sleep(3)

        step3 = '/html/body/div[1]/div[4]/section[4]/div/div[2]/div/div/div/div[2]/div[2]/div/div'
        periode = driver.find_element(By.XPATH, step3).text
        time.sleep(3)

        tanggal_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        tanggal_match = tanggal_pattern.search(periode)

        tanggal = ''
        if tanggal_match:
            tanggal = tanggal_match.group()
        else:
            print("Tidak ditemukan tanggal dalam narasi SMS.")

        now = datetime.now()
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "provider": "indosat",
            "name": name,
            "url": url_tnc,
            "startDate": now.strftime('%Y-%m-%d'),
            "endDate": tanggal,
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print("Error from hit_promo_indosat 3: ", e)


if __name__ == '__main__':
    get_promo_tokopedia()
