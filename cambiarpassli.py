import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

url='https://www.lidl.es/es/account/login?redirectTarget=previous-orders'
url2='https://www.lidl.es/es/account/manage'
boton_cookies='#CybotCookiebotDialog > div > div.cookie-alert-extended-controls > button'
selector_user='#email-login-checkout'
selector_pass='#password-login-checkout'
boton_login='#chooseaccountbutton-login-checkout'
boton_acc_mng='body > div.shifter-page > div.maxheight > section.main > div.wrapper.content.useraccount > div > aside > div > ul > li:nth-child(2) > a'
modificar_clave='body > div.shifter-page > div.maxheight > section.main > div.wrapper.content.useraccount > div > article > div > div > div:nth-child(3) > div > p > a'
selector_pass_old='#password-old-user-account'
selector_npass='#enter-new-password'
confirmar_npass='#repeat-new-password'
boton_guardar='#btn_change_password'

user='lwillh_o997h@pebih.com'
password='eO9qX0xH7'

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

driver.find_element_by_css_selector(selector_user).send_keys(user)

driver.find_element_by_css_selector(selector_pass).send_keys(password)

driver.find_element_by_css_selector(boton_login).send_keys(Keys.ENTER)

driver.refresh()

time.sleep(2)

driver.find_element_by_css_selector(selector_user).send_keys(user)

time.sleep(2)

driver.find_element_by_css_selector(selector_pass).send_keys(password)

time.sleep(2)

driver.find_element_by_css_selector(boton_login).send_keys(Keys.ENTER)

time.sleep(3)

driver.find_element_by_css_selector(boton_acc_mng).click()

time.sleep(1)

driver.find_element_by_css_selector(modificar_clave).click()

driver.find_element_by_css_selector(selector_pass_old).send_keys(password)

driver.find_element_by_css_selector(selector_npass).send_keys(npass)

driver.find_element_by_css_selector(confirmar_npass).send_keys(npass)

driver.find_element_by_css_selector(boton_guardar).click()
