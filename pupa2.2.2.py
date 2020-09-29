from selenium import webdriver
import time
import math
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_class_name('form-control')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    baton = browser.find_element_by_id("robotCheckbox")
    baton.click()

    chek = browser.find_element_by_id("robotsRule")
    chek.click()

    sub = browser.find_element_by_css_selector('[type = submit]')
    sub.click()

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()