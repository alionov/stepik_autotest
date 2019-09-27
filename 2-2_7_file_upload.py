# Импортируем вебдрайвер и прочее говно
from selenium import webdriver
import time
import os 

try:
    # Открываем ссылку
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ищем инпуты
    fname = browser.find_element_by_name("firstname")
    lname = browser.find_element_by_name("lastname")
    mail = browser.find_element_by_name("email")

    # Наваливаем в инпуты текст
    fname.send_keys("Ярополк")
    lname.send_keys("Умывальников")
    mail.send_keys("@мыльцо")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)

    # Ищем загрузку файла и заливаем туда путь к нему 
    btn1 = browser.find_element_by_id("file")
    btn1.send_keys(file_path)

    # Ищем сабмит баттон и ЖМЕМ
    sbmt_btn = browser.find_element_by_class_name("btn")
    sbmt_btn.click()
    time.sleep(10)

finally:
    browser.quit()

