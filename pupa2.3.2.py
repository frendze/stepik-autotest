from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector(".trollface.btn")
    btn1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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