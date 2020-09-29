from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(' .form-control:nth-child(2) ')
    input1.send_keys('o4ko sabaki')

    input2 = browser.find_element_by_css_selector(' .form-control:nth-child(4) ')
    input2.send_keys('o4ko sabaki')

    input3 = browser.find_element_by_css_selector(' .form-control:nth-child(6) ')
    input3.send_keys('o4ko sabaki')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'o4ko.txt')

    choosefl = browser.find_element_by_css_selector(' #file')
    choosefl.send_keys(file_path)

    sub = browser.find_element_by_css_selector(" [type = 'submit'] ")
    sub.click()



finally:
    time.sleep(10)
    browser.quit()