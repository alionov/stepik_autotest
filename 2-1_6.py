# Импортируем вебдрайвер
from selenium import webdriver

# Открываем ссылку
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

# Ищем радиобатон по ID
human_radio = browser.find_element_by_id("humanRule")

#Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
human_checked = human_radio.get_attribute("checked")
print("value of human radio: ", human_checked)
assert human_checked is not None, "Human radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robots_radio: ", robots_checked)
assert robots_checked is None