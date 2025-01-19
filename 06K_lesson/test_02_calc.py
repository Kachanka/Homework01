import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = driver.find_element(By.CSS_SELECTOR, "input#delay")
    delay.send_keys('45')

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, ".screen"), "15")

    result = driver.find_element(By.CSS_SELECTOR,'.screen').text

    assert result == 15

    driver.quit()
