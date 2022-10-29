from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_of_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    button_text = button.text

    assert len(button_text) > 0, "No add_to_cart button!"
