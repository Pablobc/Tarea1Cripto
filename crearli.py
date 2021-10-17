import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url='https://www.lidl.es/es/account/login?redirectTarget=previous-orders'
boton_cookies='#CybotCookiebotDialog > div > div.cookie-alert-extended-controls > button'
boton_registrar='#existingLoginForm > fieldset > div:nth-child(4) > div > a'
selector_user='#enter-new-email'
confirmar_user='#repeat-new-email'
selector_pass='#enter-new-password'
confirmar_pass='#repeat-new-password'
checkbox='#legal-two-newsletter-checkout'
crear_cuenta='#rp_create_account'

user='siwiro3612@smuvaj.com'
password='123456'
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

time.sleep(5)
driver.find_element_by_css_selector(boton_cookies).click()

driver.find_element_by_css_selector(boton_registrar).click()

driver.find_element_by_css_selector(selector_user).send_keys(user)

driver.find_element_by_css_selector(confirmar_user).send_keys(user)

driver.find_element_by_css_selector(selector_pass).send_keys(npass)

driver.find_element_by_css_selector(confirmar_pass).send_keys(npass)

driver.find_element_by_css_selector(checkbox).click()

driver.find_element_by_css_selector(crear_cuenta).click()
