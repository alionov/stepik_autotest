from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
btn1 = browser.find_element_by_id('book')
print('Найдена кнопка с текстом -', btn1.text)

btn1_click = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element(
        (By.ID, "price"), "$100")
    )
btn1.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id("input_value") .text
inp1 = browser.find_element_by_id("answer")
btn1 = browser.find_element_by_id("solve")

y = calc(x)
inp1.send_keys(y)
btn1.click()
time.sleep(10)