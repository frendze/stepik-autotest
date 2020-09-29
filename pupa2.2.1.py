from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    x = x_element.text
    y = y_element.text
    sum = str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    sub = browser.find_element_by_css_selector('[type = submit]')
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()