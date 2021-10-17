import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

user='lwillh_o997h@pebih.com'
password='abcABC123'

url = 'https://www.fashionspark.com/'

boton_login='body > div.page-wrapper > header > div.header.content > li > a > span'
selector_user='#email'
selector_pass='#pass'
login='#send2 > span'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_css_selector(boton_login).click()

driver.find_element_by_css_selector(selector_user).send_keys(user)

driver.find_element_by_css_selector(selector_pass).send_keys(password)

driver.find_element_by_css_selector(login).click()
