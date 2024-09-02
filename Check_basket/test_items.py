import time

import pytest
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_cart_button(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    driver.get(link)
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Button add to cart not found"
    time.sleep(10)