from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = "username"

password = "password"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element_by_id("username").send_keys(username)

driver.find_element_by_id("password"). send_keys(password)

driver.find_element_by_name("radius").click()

sleep(20)

driver.quit()
