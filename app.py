from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block  input.first")
    name.send_keys("abracadabra")
    last_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block input.second")
    last_name.send_keys("abracadabra")
    email = browser.find_element(
        By.CSS_SELECTOR, "div.first_block input.third")
    email.send_keys("abracadabra")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcomte_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcomte_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(3)
    browser.quit()


