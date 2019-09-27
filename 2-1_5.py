import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Импортируем вебдрайвер
from selenium import webdriver

# Открываем ссылку
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

# Ищем элемент, где записано значение X
x_element = browser.find_element_by_id("input_value")
# Забираем текст элемента и пристваиваем его переменной x
x = x_element.text
# подставляем переменную в формулу выше и присваиваем ответ переменной y
y = calc(x)
# Ищем поле для ввода текста на странице
input1 = browser.find_element_by_id("answer")
# Отправляем в это поле значние переменной y
input1.send_keys(y)
# Ищем ЧБ для подтверждения и жмем на него
chkbox1 = browser.find_element_by_id("robotCheckbox")
chkbox1.click()
# Ищем радиобатон и выбираем вариант с роботами
radio1 = browser.find_element_by_id("robotsRule")
radio1.click()
# Ищем кнопку и жмем на нее
btn1 = browser.find_element_by_class_name("btn-default")
btn1.click()

time.sleep(10)