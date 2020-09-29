from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name('img')
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    baton = browser.find_element_by_id("robotCheckbox")
    baton.click()

    chek = browser.find_element_by_id("robotsRule")
    chek.click()

    sub = browser.find_element_by_css_selector('[type = submit]')
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()