# Импортируем библиотеки
from selenium import webdriver
import math
import time

# Сюда подставляем полученное на странице число
def calc(valuex_num):
    return str(math.log(abs(12*math.sin(int(valuex_num)))))

# Открываем ссылку
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Ищем картинку с сундуком по ID
chest_img = browser.find_element_by_css_selector("img#treasure")

# забираем значение атрибута valuex
valuex_num = chest_img.get_attribute("valuex")
print("Значение в сундуке:", valuex_num)

# Y = результату вычисления функции
y = calc(valuex_num)
print("Y =", y)

# Ищем поле для ввода текста по ID и обзываем его input и вводим туда Y
input = browser.find_element_by_id("answer")
input.send_keys(y)
time.sleep(1)

# Ищем ЧБ и кликаем по нему
chek_box = browser.find_element_by_id("robotCheckbox")
chek_box.click()
time.sleep(1)

# Ищем радиобатон и кликаем по robots rule
radiobaton = browser.find_element_by_id("robotsRule")
radiobaton.click()
time.sleep(1)

# Ищем кнопку и жмем на нее
btn1 = browser.find_element_by_class_name("btn-default")
btn1.click()
time.sleep(10)