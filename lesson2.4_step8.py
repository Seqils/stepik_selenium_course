import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    value_x = browser.find_element(By.ID, "input_value")
    x = value_x.text
    y = calc(x)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)

    button2 = browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(15)

    browser.quit()
