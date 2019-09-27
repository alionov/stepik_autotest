from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
button = browser.find_element(By.ID, "submit_button")