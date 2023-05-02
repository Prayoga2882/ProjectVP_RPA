import time
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
from tkinter import messagebox


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


def generate_promo_telkomsel():
    downloaded = trafilatura.fetch_url('https://www.telkomsel.com/promo')
    soup = BeautifulSoup(downloaded, 'html.parser')
    element_rate = soup.find_all('div', class_='promo-name')
    # name
    name = []
    for i in element_rate:
        if i.text != '':
            name.append(i.text)
    try:
        hit_promoTSEL1(name)
    except:
        try:
            hit_promoTSEL2(name)
        except:
            try:
                hit_promoTSEL3(name)
            except:
                hit_promoTSEL4(name)
                try:
                    hit_promoTSEL5(name)
                except:
                    hit_promoTSEL6(name)

    messagebox.showinfo("Success", "Promo Telkomsel has been generated!")


def hit_promoTSEL1(name):
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    url_tnc = driver.current_url

    try:
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
        print(e)
        raise Exception(" Except error from hit_promo1")


def hit_promoTSEL2(name):
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    url_tnc = driver.current_url
    try:
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
        print(e)
        raise Exception(" Except error from hit_promo2")


def hit_promoTSEL3(name):
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    url_tnc = driver.current_url
    try:
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
        print(e)
        raise Exception(" Except error from hit_promo3")


def hit_promoTSEL4(name):
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    url_tnc = driver.current_url
    try:
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
        print(e)
        raise Exception(" Except error from hit_promo4")


def hit_promoTSEL5(name):
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    url_tnc = driver.current_url
    try:
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
        print(e)
        raise Exception(" Except error from hit_promo5")


def hit_promoTSEL6(name):
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

    click2 = '/html/body/div[5]/div[2]/div/div/div/div/div[4]/div/div/div/div[4]/div[1]/p'
    driver.find_element(By.XPATH, click2).click()
    time.sleep(3)

    url_tnc = driver.current_url
    try:
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
        print(e)
        raise Exception(" Except error from hit_promo6")


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


def generate_promo_axis():
    hit_promoAXIS1()
    hit_promoAXIS2()

    messagebox.showinfo("Success", "Promo Axis has been generated!")


def hit_promoAXIS1():
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

    step3 = '/html/body/section[1]/div/div/div/div[2]/p[2]'
    periode = driver.find_element(By.XPATH, step3).text
    result_periode = periode_format_axis(periode)

    url_tnc = driver.current_url

    try:
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
        print(e)
        raise Exception(" Except error from hit_promoAXIS1")

    hit_promoAXIS2()
    driver.quit()


def hit_promoAXIS2():
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
    result_periode = periode_format_axis(periode)

    url_tnc = driver.current_url
    try:
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
        print(e)
        raise Exception(" Except error from hit_promoAXIS2")

    driver.quit()


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
    # data = "Periode Program: 1 – 30 April 2023"

    # menghapus kata "Periode Program"
    data = data.replace("Periode Program: ", "")
    data = data.replace("Periode Promo: ", "")

    # split tanggal menjadi start date dan end date
    tanggal = data.split(" – ")

    # pastikan jumlah elemen di dalam tanggal adalah 2
    if len(tanggal) < 2:
        return None

    start_date_str = tanggal[0] + " April 2023"
    end_date_str = tanggal[1].replace("April 2023", "") + "April 2023"

    # ubah format tanggal menggunakan datetime
    start_date = datetime.strptime(start_date_str, '%d %B %Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%d %B %Y').strftime('%Y-%m-%d')

    # simpan hasil dalam dictionary
    hasil = {
        "startDate": start_date,
        "endDate": end_date
    }

    return hasil


def generate_promo_indosat():
    hit_promo_isat1()
    hit_promo_isat2()


def hit_promo_isat1():
    url = "https://indosatooredoo.com/portal/id/pspromolanding"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    step3 = '/html/body/div[1]/div[4]/section[3]/div/div[2]/div/div/div/div[3]/div[1]/a'
    driver.find_element(By.XPATH, step3).click()
    time.sleep(3)

    step4 = '/html/body/div[1]/div[4]/section[3]/div/div[2]/div/div/div/div[3]/div[2]/div/div'
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

    try:
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
        print(e)
        raise Exception(" Except error from hit_promo_indosat_1")
    driver.quit()


def hit_promo_isat2():
    url = "https://www.indosatooredoo.com/portal/id/pspromo_inboundroaming"
    # chrome_options = chrome_option()
    driver = webdriver.Chrome()
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

    try:
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
        print(e)
        raise Exception(" Except error from hit_promo_indosat_2")
    driver.quit()


if __name__ == '__main__':
    generate_promo_indosat()
