import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

user='lwillh_o997h@pebih.com'
password='qV8oQ2eG5'

url = 'https://www.fashionspark.com/'
url2='https://fashionspark.com/customer/account/'
boton_login='body > div.page-wrapper > header > div.header.content > li > a > span'
selector_user='#email'
selector_pass='#pass'
login='#send2 > span'
boton_cambio='#maincontent > div.columns > div.column.main > div.block.block-dashboard-info > div.block-content > div.box.box-information > div.box-actions > a.action.change-password'
selector_pass_actual='#current-password'
selector_nueva_pass='#password'
selector_confirmar='#password-confirmation'
guardar='#form-validate > div > div.primary > button'


minusculas='abcdefghijklmnopqrstuvwxyz'
mayusculas='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digitos='0123456789'

npass=''
for i in range(3):
    npass+=random.choice(minusculas)+random.choice(mayusculas)+random.choice(digitos)

print(npass)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_css_selector(boton_login).click()

time.sleep(10)

driver.find_element_by_css_selector(selector_user).send_keys(user)

driver.find_element_by_css_selector(selector_pass).send_keys(password)

driver.find_element_by_css_selector(login).click()

driver.get(url2)

driver.find_element_by_css_selector(boton_cambio).click()

driver.find_element_by_css_selector(selector_pass_actual).send_keys(password)

driver.find_element_by_css_selector(selector_nueva_pass).send_keys(npass)

driver.find_element_by_css_selector(selector_confirmar).send_keys(npass)

time.sleep(5)

driver.find_element_by_css_selector(guardar).click()

time.sleep(2)

driver.find_element_by_css_selector(guardar).click()
