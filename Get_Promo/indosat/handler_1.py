from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from helper.index import chrome_option


def ISAT1():
    url = 'https://indosatooredoo.com/portal/id/pssensasi'
    chrome_options = chrome_option()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    name = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/section[1]/div/div/h3").text

    driver.execute_script("window.scrollTo({top: document.body.scrollHeight * 0.5, behavior: 'smooth'});")
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/section[3]/div/div[2]/div/div/div/div[3]/div[1]/a").click()
    time.sleep(3)
    xpath_periode = "/html/body/div[1]/div[4]/section[3]/div/div[2]/div/div/div/div[3]/div[2]/div/div"
    periode = driver.find_element(By.XPATH, xpath_periode).text

    driver.close()

    return name, periode, 'Tidak syarat dan ketentuan'


if __name__ == '__main__':
    result = ISAT1()
    print(result)
