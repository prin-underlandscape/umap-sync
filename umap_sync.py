import pytest
import time
import json
import os, sys
from urllib.request import urlretrieve, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


def sync(dataset_name):
# Download dataset geojsos and extract URL of umap map
  with urlopen(f"https://raw.githubusercontent.com/prin-underlandscape/{dataset_name}/main/{dataset_name}.geojson") as content:
    umap_url = json.load(content)["properties"]["umapKey"]
# Download umap and store as a file to be uploaded to umap service 
  urlretrieve(f"https://raw.githubusercontent.com/prin-underlandscape/{dataset_name}/main/{dataset_name}.umap",'./dataset.umap')
  print(f"Syncing {umap_url}") 
  driver.find_element(By.PARTIAL_LINK_TEXT, "Dashboard")
  driver.get(umap_url)
  driver.find_element(By.CSS_SELECTOR, ".leaflet-control-edit-enable > button").click()
  driver.find_element(By.CSS_SELECTOR, ".update-map-settings").click()
  driver.find_element(By.CSS_SELECTOR, "details:nth-child(11) > summary").click()
  driver.find_element(By.CSS_SELECTOR, ".umap-empty:nth-child(2)").click()
  driver.find_element(By.CSS_SELECTOR, ".buttons:nth-child(1) .icon-close").click()
  driver.find_element(By.CSS_SELECTOR, ".upload-data").click()

  upload_file = os.path.abspath("./dataset.umap")
  file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
  file_input.send_keys(upload_file)
  driver.find_element(By.NAME, "submit").click()
  driver.find_element(By.CSS_SELECTOR, ".buttons:nth-child(1) .icon-close").click()
  driver.find_element(By.CSS_SELECTOR, ".leaflet-control-edit-save").click()
  print("ecco")

  time.sleep(10)	

if len(sys.argv) < 2:
  exit("Bisogna passare i dataset da sincronizzare")

# Browser configuration
chrome_service = Service(executable_path='/snap/chromium/2890/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=chrome_service)
driver.set_window_size(1600,900)
driver.implicitly_wait(60) # useful to wait for login
# Start from login page
driver.get("https://umap.openstreetmap.fr/it/login/")

for dataset in sys.argv[1:]:
  print(f"Sincronizzo il dataset {dataset}")
  sync(dataset.split('.')[0])
