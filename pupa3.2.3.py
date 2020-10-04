import unittest
import time
from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ищем все input'ы c атрибутом обязательного заполнения
        elements = browser.find_elements_by_tag_name("input[required]")
        print("Число найденных элементов: ", len(elements))

        # Заполняем ответы
        for element in elements:
            element.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!", "o4ko sobaki")

        # успеваем увидеть ответ за 3 секунды
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

        # не забываем оставить пустую строку в конце файла
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ищем все input'ы c атрибутом обязательного заполнения
        elements = browser.find_elements_by_tag_name("input[required]")
        print("Число найденных элементов: ", len(elements))

        # Заполняем ответы
        for element in elements:
            element.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h2")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text,"Congratulations! You have successfully registered! ", "o4ko sobaki")

        # успеваем увидеть ответ за 3 секунды
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

        # не забываем оставить пустую строку в конце файла

if __name__ == "__main__":
    unittest.main()

#FAILED (errors=1)- ответ , так как я неправильно сделал задание ранее - у меня на 2 страницах не падал тест,
# поэтому во втором тесте при поиске селектора текста успеха я выставил заранее неверный селектор h2 - тест упал с нужной ошибкой