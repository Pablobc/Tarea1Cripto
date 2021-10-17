import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


url = 'https://www.fashionspark.com/'
boton_login='body > div.page-wrapper > header > div.header.content > li > a > span'
boton_crear='#maincontent > div.columns > div > div.login-container > div.block.block-new-customer > div.block-content > div > div > a > span'
selector_nombre='#firstname'
selector_apellido='#lastname'
selector_user='#email_address'
selector_pass='#password'
selector_confirmar='#password-confirmation'
boton_crear_cuenta='#form-validate > div > div.primary > button > span'

email='siwiro3612@smuvaj.com'
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

driver.find_element_by_css_selector(boton_crear).click()

driver.find_element_by_css_selector(selector_nombre).send_keys('Maria')

driver.find_element_by_css_selector(selector_apellido).send_keys('Pinto')

driver.find_element_by_css_selector(selector_user).send_keys(email)

driver.find_element_by_css_selector(selector_pass).send_keys(npass)

driver.find_element_by_css_selector(selector_confirmar).send_keys(npass)

time.sleep(3)

driver.find_element_by_css_selector(boton_crear_cuenta).click()
time.sleep(2)
driver.find_element_by_css_selector(boton_crear_cuenta).click()
