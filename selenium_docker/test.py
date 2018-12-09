from selenium import webdriver
from time import sleep 
import os 

print(os.environ['CHROME_DRIVER'])
driver = webdriver.Chrome(os.environ['CHROME_DRIVER'])
driver.get('http://www.google.com')


