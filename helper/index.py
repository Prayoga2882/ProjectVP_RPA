import json
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import trafilatura
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from tkinter import messagebox


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
    # data = '18 April - 30 April 2023'
    date_range, year = data.rsplit(" ", 1)
    start_date_str, end_date_str = date_range.split(" - ")

    output = {
        "startDate": f"{year.strip()}-{get_month_number(start_date_str.split()[1])}-{start_date_str.split()[0]}",
        "endDate": f"{year.strip()}-{get_month_number(end_date_str.split()[1])}-{end_date_str.split()[0]}"
    }
    return output


def show_messagebox(root):
    messagebox.showinfo("Message", "Hello, World!")
    root.destroy()


def telkomsel_core():
    downloaded = trafilatura.fetch_url('https://www.telkomsel.com/promo')
    soup = BeautifulSoup(downloaded, 'html.parser')
    element_rate = soup.find_all('div', class_='promo-name')
    # name
    name = []
    for i in element_rate:
        if i.text != '':
            name.append(i.text)

    hit_promo1(name)
    hit_promo2(name)
    hit_promo3(name)
    hit_promo4(name)
    hit_promo5(name)
    hit_promo6(name)


def hit_promo1(name):
    url = "https://www.telkomsel.com/promo"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    tnc = '//*[@id="accordionA4"]'
    result_tnc = driver.find_element(By.XPATH, tnc).text
    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name[0],
            "tnc": result_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from hit_promo1")


def hit_promo2(name):
    url = "https://www.telkomsel.com/promo"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    tnc = '//*[@id="accordionA4"]'
    result_tnc = driver.find_element(By.XPATH, tnc).text
    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name[1],
            "tnc": result_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from hit_promo2")


def hit_promo3(name):
    url = "https://www.telkomsel.com/promo"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    tnc = '//*[@id="accordionA4"]'
    result_tnc = driver.find_element(By.XPATH, tnc).text
    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name[2],
            "tnc": result_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from hit_promo3")


def hit_promo4(name):
    url = "https://www.telkomsel.com/promo"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    tnc = '//*[@id="accordionA4"]'
    result_tnc = driver.find_element(By.XPATH, tnc).text
    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name[3],
            "tnc": result_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from hit_promo4")


def hit_promo5(name):
    url = "https://www.telkomsel.com/promo"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    tnc = '//*[@id="accordionA4"]'
    result_tnc = driver.find_element(By.XPATH, tnc).text
    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name[4],
            "tnc": result_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from hit_promo5")


def hit_promo6(name):
    url = "https://www.telkomsel.com/promo"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    tnc = '//*[@id="accordionA4"]'
    result_tnc = driver.find_element(By.XPATH, tnc).text
    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name[5],
            "tnc": result_tnc,
            "startDate": periode["startDate"],
            "endDate": periode["endDate"],
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from hit_promo6")


def scroll_25(driver):
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.25, behavior: 'smooth'});")
    time.sleep(3)


def get_month_number(month):
    months = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    return months[month]


if __name__ == '__main__':
    telkomsel_core()
