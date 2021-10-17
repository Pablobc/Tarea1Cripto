import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

url='https://www.lidl.es/es/account/login?redirectTarget=previous-orders'

boton_olvidaste='#do-not-remember-general-login'
selector_user='#email-remember-general-login'
boton_submit='#resetPasswordForm > fieldset > div:nth-child(4) > button'
boton_cookies='#CybotCookiebotDialog > div > div.cookie-alert-extended-controls > button'

user='lwillh_o997h@pebih.com'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(5)
driver.find_element_by_css_selector(boton_cookies).click()

driver.find_element_by_css_selector(boton_olvidaste).click()

driver.find_element_by_css_selector(selector_user).send_keys(user)

driver.find_element_by_css_selector(boton_submit).click()

driver.refresh()

driver.find_element_by_css_selector(boton_olvidaste).click()

driver.find_element_by_css_selector(selector_user).send_keys(user)

driver.find_element_by_css_selector(boton_submit).click()
