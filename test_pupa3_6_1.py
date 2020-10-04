import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1"," https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    browser.implicitly_wait(20)
    link = f"{links}"
    browser.get(link)

    answer = math.log(int(time.time()))
    y=str(answer)
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    apruve = browser.find_element_by_css_selector(".smart-hints__hint")

    assert apruve.text == "Correct!" , f"{apruve.text}"
    time.sleep(1)
