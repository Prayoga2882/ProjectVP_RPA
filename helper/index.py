import json


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
