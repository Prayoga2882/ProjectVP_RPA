from helper.index import *
from conf.xpath_conf import sukma_convert


def get_rate_via_pulsa():
    try:
        url = 'https://www.viapulsa.com/'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.25, behavior: 'smooth'});")
        time.sleep(3)

        rate = '/html/body/div[2]/main/div/section[3]/div/div/div/section'
        rate = driver.find_element(By.XPATH, rate).text
        rate = rate.split('\n')

        result = {
            "company": "VIA PULSA",
            "rate": []
        }

        for i in range(0, len(rate), 2):
            result["rate"].append({rate[i]: rate[i + 1]})

        data = json.dumps(result)
        payload = json.loads(data)

        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success Generate Rate VIA PULSA")
    except Exception as e:
        print("Except error from rate via pulsa", e)


def get_rate_by_pulsa():
    try:
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

        for i in range(len(payload['rate'])):
            for key, value in payload['rate'][i].items():
                payload['rate'][i][key] = float(value.replace('%', '')) / 100

        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success Generate Rate BY PULSA")
    except Exception as e:
        print("Except error from rate by pulsa", e)


def get_rate_conversa():
    try:
        url = 'https://conversa.trikersdev.com/'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.70, behavior: 'smooth'});")
        time.sleep(3)

        # ========= XL/Axis ========== #
        rate_xl_axis = '/html/body/div[5]/div[2]/div[2]/div[2]/div/div[1]/div'
        rate_xl_axis = driver.find_element(By.XPATH, rate_xl_axis).text.split("\n")
        time.sleep(3)

        rate_xl_axis[1] = rate_xl_axis[1].replace('%', '')
        del rate_xl_axis[2:]

        # ========= TELKOMSEL ========== #
        rate_tsel = '/html/body/div[5]/div[2]/div[2]/div[2]/div/div[2]/div'
        rate_tsel = driver.find_element(By.XPATH, rate_tsel).text.split("\n")
        time.sleep(3)

        rate_tsel[1] = rate_tsel[1].replace('%', '')
        del rate_tsel[2:]

        # ========= Three ========== #
        rate_three = '/html/body/div[5]/div[2]/div[2]/div[2]/div/div[3]/div'
        rate_three = driver.find_element(By.XPATH, rate_three).text.split("\n")
        time.sleep(3)

        rate_three[1] = rate_three[1].replace('%', '')
        del rate_three[2:]

        # ========= Indosat ========== #
        rate_indosat = '/html/body/div[5]/div[2]/div[2]/div[2]/div/div[4]/div'
        rate_indosat = driver.find_element(By.XPATH, rate_indosat).text.split("\n")
        time.sleep(3)

        rate_indosat[1] = rate_indosat[1].replace('%', '')
        del rate_indosat[2:]

        # ========= Smartfren ========== #
        rate_smartfren = '/html/body/div[5]/div[2]/div[2]/div[2]/div/div[5]/div'
        rate_smartfren = driver.find_element(By.XPATH, rate_smartfren).text.split("\n")
        time.sleep(3)

        rate_smartfren[1] = rate_smartfren[1].replace('%', '')
        del rate_smartfren[2:]

        # ========= By.U ========== #
        rate_byu = '/html/body/div[5]/div[2]/div[2]/div[2]/div/div[6]/div'
        rate_byu = driver.find_element(By.XPATH, rate_byu).text.split("\n")
        time.sleep(3)

        rate_byu[1] = rate_byu[1].replace('%', '')
        del rate_byu[2:]

        result = {
            'company': 'CONVERSA',
            'rate': [
                {
                    rate_xl_axis[0]: "{:.2f}".format(float(rate_xl_axis[1]) / 100)
                },
                {
                    rate_tsel[0]: "{:.2f}".format(float(rate_tsel[1]) / 100)
                },
                {
                    rate_three[0]: "{:.2f}".format(float(rate_three[1]) / 100)
                },
                {
                    rate_indosat[0]: "{:.2f}".format(float(rate_indosat[1]) / 100)
                },
                {
                    rate_smartfren[0]: "{:.2f}".format(float(rate_smartfren[1]) / 100)
                },
                {
                    rate_byu[0]: "{:.2f}".format(float(rate_byu[1]) / 100)
                }
            ]
        }

        result = json.dumps(result)
        payload = json.loads(result)

        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success Generate Rate CONVERSA")

    except Exception as e:
        print("Except error from rate conversa", e)


def get_rate_sulap_pulsa():
    try:
        url = 'https://sulap-pulsa.id/'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.20, behavior: 'smooth'});")
        time.sleep(3)

        result = {
            "company": "SULAP PULSA",
            "rate": []
        }

        # ========= Indosat ========== #
        rate_indosat = '/html/body/section[2]/div/div[2]/div/div/div[1]'
        rate_indosat = driver.find_element(By.XPATH, rate_indosat).text.split("\n")
        time.sleep(3)
        rate_indosat.pop()
        for i in range(0, len(rate_indosat), 2):
            key = "Indosat " + rate_indosat[i + 1].replace("* ", "")
            value = rate_indosat[i]
            result["rate"].append({key: value})

        # ========= XL ========== #
        ratexl = '/html/body/section[2]/div/div[2]/div/div/div[2]'
        ratexl = driver.find_element(By.XPATH, ratexl).text.split("\n")
        time.sleep(3)
        ratexl.pop()
        for i in range(0, len(ratexl), 2):
            key = "XL " + ratexl[i + 1].replace("* ", "")
            value = ratexl[i]
            result["rate"].append({key: value})

        # ========= Telkomsel ========== #
        ratetelkomsel = '/html/body/section[2]/div/div[2]/div/div/div[3]'
        ratetelkomsel = driver.find_element(By.XPATH, ratetelkomsel).text.split("\n")
        time.sleep(3)
        ratetelkomsel.pop()
        for i in range(0, len(ratetelkomsel), 2):
            key = "Telkomsel " + ratetelkomsel[i + 1].replace("* ", "")
            value = ratetelkomsel[i]
            result["rate"].append({key: value})

        # ========= Axis ========== #
        rateaxis = '/html/body/section[2]/div/div[2]/div/div/div[4]'
        rateaxis = driver.find_element(By.XPATH, rateaxis).text.split("\n")
        time.sleep(3)
        rateaxis.pop()
        for i in range(0, len(rateaxis), 2):
            key = "Axis " + rateaxis[i + 1].replace("* ", "")
            value = rateaxis[i]
            result["rate"].append({key: value})

        # ========= Three ========== #
        ratethree = '/html/body/section[2]/div/div[2]/div/div/div[5]'
        ratethree = driver.find_element(By.XPATH, ratethree).text.split("\n")
        time.sleep(3)
        ratethree.pop()
        for i in range(0, len(ratethree), 2):
            key = "Three " + ratethree[i + 1].replace("* ", "")
            value = ratethree[i]
            result["rate"].append({key: value})

        # ========= Smartfren ========== #
        ratesmartfren = '/html/body/section[2]/div/div[2]/div/div/div[6]'
        ratesmartfren = driver.find_element(By.XPATH, ratesmartfren).text.split("\n")
        time.sleep(3)
        ratesmartfren.pop()
        for i in range(0, len(ratesmartfren), 2):
            key = "Smartfren " + ratesmartfren[i + 1].replace("* ", "")
            value = ratesmartfren[i]
            result["rate"].append({key: value})

        # ========= Byu ========== #
        ratebyu = '/html/body/section[2]/div/div[2]/div/div/div[7]'
        ratebyu = driver.find_element(By.XPATH, ratebyu).text.split("\n")
        time.sleep(3)
        ratebyu.pop()
        for i in range(0, len(ratebyu), 2):
            key = "Byu " + ratebyu[i + 1].replace("* ", "")
            value = ratebyu[i]
            result["rate"].append({key: value})

        result = json.dumps(result)
        payload = json.loads(result)
        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success Generate rate SULAP PULSA")
    except Exception as e:
        print("Except error from rate sulap pulsa", e)


def get_rate_tentra_pulsa():
    try:
        url = 'https://tetrapulsa.com/'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.25, behavior: 'smooth'});")
        time.sleep(3)

        # ========= TELKOMSEL ========== #
        rate_tsel = '/html/body/div[1]/main/div/section[2]/div[2]/div/div[2]/div'
        rate_tsel = driver.find_element(By.XPATH, rate_tsel).text.split("\n")
        time.sleep(3)
        rate_tsel.remove('TUKAR PULSA')
        rate_tsel.remove('HUBUNGI KAMI')
        rate_tsel.remove('Telkomsel')

        cleaned_data = [d.strip().replace('\u2013', '-').replace(',', '.') for d in rate_tsel]

        formatted_data = {'company': 'TENTRA PULSA', 'rate': []}

        for i in range(0, len(cleaned_data), 2):
            if i + 1 < len(cleaned_data):
                rate_tsel = {f'Telkomsel {cleaned_data[i]}': cleaned_data[i + 1]}
                formatted_data['rate'].append(rate_tsel)

        # ========= Three ========== #
        rate_three = '/html/body/div[1]/main/div/section[2]/div[2]/div/div[3]/div'
        rate_three = driver.find_element(By.XPATH, rate_three).text.split("\n")
        time.sleep(3)
        rate_three.remove('TUKAR PULSA')
        rate_three.remove('HUBUNGI KAMI')
        rate_three.remove('Three')

        cleaned_data = [d.strip().replace('\u2013', '-').replace(',', '.') for d in rate_three]

        for i in range(0, len(cleaned_data), 2):
            if i + 1 < len(cleaned_data):
                rate_three = {f'Three {cleaned_data[i]}': cleaned_data[i + 1]}
                formatted_data['rate'].append(rate_three)

        # ========= XL ========== #
        ratexl = '/html/body/div[1]/main/div/section[2]/div[2]/div/div[4]/div'
        ratexl = driver.find_element(By.XPATH, ratexl).text.split("\n")
        time.sleep(3)
        ratexl.remove('TUKAR PULSA')
        ratexl.remove('HUBUNGI KAMI')
        ratexl.remove('XL')

        cleaned_data = [d.strip().replace('\u2013', '-').replace(',', '.') for d in ratexl]

        for i in range(0, len(cleaned_data), 2):
            if i + 1 < len(cleaned_data):
                ratexl = {f'XL {cleaned_data[i]}': cleaned_data[i + 1]}
                formatted_data['rate'].append(ratexl)

        # ========= Axis ========== #
        rateaxis = '/html/body/div[1]/main/div/section[2]/div[2]/div/div[5]/div'
        rateaxis = driver.find_element(By.XPATH, rateaxis).text.split("\n")
        time.sleep(3)
        rateaxis.remove('TUKAR PULSA')
        rateaxis.remove('HUBUNGI KAMI')
        rateaxis.remove('Axis')

        cleaned_data = [d.strip().replace('\u2013', '-').replace(',', '.') for d in rateaxis]

        for i in range(0, len(cleaned_data), 2):
            if i + 1 < len(cleaned_data):
                rateaxis = {f'Axis {cleaned_data[i]}': cleaned_data[i + 1]}
                formatted_data['rate'].append(rateaxis)

        result = json.dumps(formatted_data)
        payload = json.loads(result)

        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success Generate rate TENTRA PULSA")

    except Exception as e:
        print("Except error from rate conversa", e)


def get_rate_cv_convert():
    try:
        url = 'https://www.cvpulsa.id/'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        rate = "/html/body/div[3]/div/div[3]/div/div/div"
        rate = driver.find_element(By.XPATH, rate).text.split("\n")
        time.sleep(3)

        result = {'company': 'CV PULSA', "rate": []}

        for i in range(len(rate)):
            if i == 0:
                result['rate'].append({'Telkomsel': rate[i]})
            elif i == 1:
                result['rate'].append({'XL': rate[i]})
            elif i == 2:
                result['rate'].append({'Indosat': rate[i]})
            elif i == 3:
                result['rate'].append({'Tri': rate[i]})

        result = json.dumps(result)
        payload = json.loads(result)
        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success get rate from CV CONVERT")
    except Exception as e:
        print("Except error from zona convert", e)


def get_rate_zahra_convert():
    try:
        url = 'https://www.zahraconvert.com/'
        chrome_options = chrome_option()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(3)

        driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.3, behavior: 'smooth'});")
        time.sleep(3)

        result = {'company': 'ZAHRA CONVERT', "rate": []}

        # ========================================================================================== #
        rate = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[1]"
        rate = driver.find_element(By.XPATH, rate).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate})

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                result['rate'].append(rate_item)

        # ========================================================================================== #
        rate_tri = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[2]"
        rate_tri = driver.find_element(By.XPATH, rate_tri).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate_tri})

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                result['rate'].append(rate_item)

        # ========================================================================================== #
        rate_isat = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[3]"
        rate_isat = driver.find_element(By.XPATH, rate_isat).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate_isat})

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                result['rate'].append(rate_item)

        # ========================================================================================== #
        rate_xl_axis = "/html/body/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[4]"
        rate_xl_axis = driver.find_element(By.XPATH, rate_xl_axis).text
        time.sleep(3)

        rate_dict = {"rate": []}
        rate_dict["rate"].append({"rate": rate_xl_axis})

        for item in rate_dict['rate']:
            rate_str = item['rate'].split('\n')
            company = rate_str.pop(0)

            for i in range(0, len(rate_str), 2):
                rate_item = {}
                rate_item[company + ' ' + rate_str[i]] = rate_str[i + 1]
                result['rate'].append(rate_item)

        payload = json.dumps(result)
        payload = json.loads(payload)
        url = 'https://ratepromo.vercel.app/rate'
        response = requests.post(url, json=payload)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success Generate rate ZAHRA CONVERT")

    except Exception as e:
        print("Except error from rate zahra convert :", e)


def get_rate_sukma_convert():
    try:
        url = 'https://www.sukmaconvert.com/'
        # chrome_options = chrome_option()
        driver = webdriver.Chrome()
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

        new_rate_list = []
        for rate in rate_dict['rate']:
            for k, v in rate.items():
                k = k.replace('/', ' ')
                for item in re.findall(r'\d+\w+-\d+\w+', v):
                    value = re.search(f'{item} (\S+)', v).group(1)
                    new_rate_list.append({f"{k} {item}": value})

        result = {"company": rate_dict['company'], "rate": new_rate_list}
        final = json.dumps(result)
        final = json.loads(final)

        for item in final["rate"]:
            for key in item:
                item[key] = float(item[key].strip("%")) / 100

        if not final:
            print("No data from sukma convert")

        url = 'https://ratepromo.vercel.app/rate'

        response = requests.post(url, json=final)
        print('Status Code:', response.status_code)
        print('Response:', response.json())

        print("Success", "Success Generate rate SUKMA CONVERT")
    except Exception as e:
        print("Except error from rate sukma convert", e)


if __name__ == '__main__':
    # get_rate_via_pulsa()
    # get_rate_by_pulsa()
    # get_rate_sukma_convert()
    # get_rate_zahra_convert()
    # get_rate_cv_convert()
    # get_rate_tentra_pulsa()
    # get_rate_conversa()
    get_rate_sulap_pulsa()
