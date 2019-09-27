# Импортируем вебдрайвер и прочее говно
from selenium import webdriver
import time
import math

try:
    # открываем ссыль в хромце
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем и жмем кнопку
    btn = browser.find_element_by_class_name("btn-primary")
    btn.click()
    time.sleep(1)

    # Идем в модалку и жмем ок
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    # Оказываемся на новой странице и забираем x, инпут и кнопку
    x = browser.find_element_by_id("input_value") .text
    inp1 = browser.find_element_by_class_name("form-control")
    btn1 = browser.find_element_by_class_name("btn-primary")

    # Считаем y
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # Записываем y в инпут и жмем батон
    inp1.send_keys(y)
    btn1.click()
    time.sleep(10)

finally:
    browser.quit()