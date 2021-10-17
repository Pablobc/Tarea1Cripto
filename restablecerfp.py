import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

user='lwillh_o997h@pebih.com'
url = 'https://www.fashionspark.com/'
boton_login='body > div.page-wrapper > header > div.header.content > li > a > span'
boton_restablecer='#login-form > fieldset > div.actions-toolbar > div.secondary > a > span'
selector_user='#email_address'
boton_send='#form-validate > div > div.primary > button > span'
boton_close='body > div.fancybox-overlay.fancybox-overlay-fixed > div > div > a'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_css_selector(boton_login).click()
driver.find_element_by_css_selector(boton_restablecer).click()
driver.find_element_by_css_selector(selector_user).send_keys(user)
driver.find_element_by_css_selector(boton_close).click()
driver.find_element_by_css_selector(boton_send).click()
