from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def get_elements():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "https://bima.tri.co.id/home"
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH,
                        '/html/body/ngb-modal-window/div/div/app-notification-confirmation/div/div[3]/div/a[1]').click()

    elems = driver.execute_script(
        "return document.getElementsByClassName('swiper-wrapper')")
    time.sleep(5)
    for elem in elems:
        print(elem.text)

    driver.quit()


if __name__ == '__main__':
    get_elements()
