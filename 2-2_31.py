# Импортируем вебдрайвер и прочее говно
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

try:
    # Открываем ссылку
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем числf и присваеваем их переменным x и y
    x = browser.find_element_by_id("num1") .text
    y = browser.find_element_by_id("num2") .text

    # Складываем переменные, обзываем их z и конвертим в строку
    z = str(int(x) + int(y))
    print(x, "+", y, "=", z)

    # Ищем выпадающее меню и выбираем пункт равный z
    drop = Select(browser.find_element_by_id("dropdown"))
    drop.select_by_value(z)
    time.sleep(1)

    # Ищем кнопку и жмем ее со всей дури
    btn1 = browser.find_element_by_class_name("btn-default")
    btn1.click()
    time.sleep(10)

finally:
    browser.quit()