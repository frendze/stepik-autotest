from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(12)

    cena = WebDriverWait(browser, 12).until( EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    print(cena)

    book = browser.find_element_by_id('book')
    book.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    sub = browser.find_element_by_css_selector(" [type = 'submit'] ")
    sub.click()



finally:
    time.sleep(10)
    browser.quit()