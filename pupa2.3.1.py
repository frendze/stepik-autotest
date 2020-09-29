from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector(" .btn ")
    btn1.click()

    alert = browser.switch_to.alert
    alert.accept()

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