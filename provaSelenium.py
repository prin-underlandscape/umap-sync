import pytest
import time
import json
import os
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


chrome_service = Service(executable_path='/snap/chromium/2890/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=chrome_service)
driver.set_window_size(1556, 840)
WebDriverWait wait = new WebDriverWait(driver, 5)

driver.get("https://umap.openstreetmap.fr/it/login/")

someVariable = getpass.getpass("Press Enter after You are done logging in")



driver.get("https://umap.openstreetmap.fr/it/map/fase1-240214-aiolasangiorgio_1087280")
driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, ".leaflet-control-edit-enable > button").click()
driver.find_element(By.CSS_SELECTOR, ".update-map-settings").click()
driver.find_element(By.CSS_SELECTOR, "details:nth-child(11) > summary").click()
driver.find_element(By.CSS_SELECTOR, ".umap-empty:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".buttons:nth-child(1) .icon-close").click()
driver.find_element(By.CSS_SELECTOR, ".upload-data").click()


upload_file = os.path.abspath("/tmp/umap.umap")

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)

driver.find_element(By.NAME, "submit").click()

#element = driver.find_element(By.CSS_SELECTOR, "body")
driver.find_element(By.CSS_SELECTOR, ".buttons:nth-child(1) .icon-close").click()
driver.find_element(By.CSS_SELECTOR, ".leaflet-control-edit-save").click()

time.sleep(3)
