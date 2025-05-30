from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.jumia.com.ng/")
print("Successfully opened Jumia website.")
time.sleep(5)