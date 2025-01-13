import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_03_shop(driver):
    driver.get("https://www.saucedemo.com/")

    user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    user_name.clear()
    user_name.send_keys('standart_user')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.clear()
    password.send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(By.CSS_SELECTOR, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "add-to-cart-sauce-labs-onesize").click()

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    driver.find_element(By.CSS_SELECTOR, "checkout").click()

    first_name = driver.find_element(By.CSS_SELECTOR, "first-name")
    first_name.clear()
    first_name.send_keys('Александра')
    last_name = driver.find_element(By.CSS_SELECTOR, "last_name")
    last_name.clear()
    last_name.send_keys('Качанова')
    postal_code = driver.find_element(By.CSS_SELECTOR, "postal-code")
    postal_code.clear()
    postal_code.send_keys('620141')

    driver.find_element(By.CSS_SELECTOR, "continue").click()

    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text()
    print(total)

    return total

def test_total(driver):
    assert test_purchase_total(driver) == 'Total $58.29'
    
