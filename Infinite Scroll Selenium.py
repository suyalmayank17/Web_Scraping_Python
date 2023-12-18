from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url = "https://www.ajio.com/men-jackets-coats/c/830216010"
s = Service("C:/Users/Mayank/Web Scraping/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get(url)
time.sleep(4)
height = driver.execute_script("return document.body.scrollHeight")
while True:
    # print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    height = new_height
    