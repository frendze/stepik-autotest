from selenium import webdriver
import time 

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")
    time.sleep(10)