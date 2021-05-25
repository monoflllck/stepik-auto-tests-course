from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from calc import calc
import time

url = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(url)

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    x = calc(x)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(x)

    button = browser.find_element(By.ID, "solve").click()

    alert = browser.switch_to.alert 
    alert_text = alert.text
    print(alert_text)
    alert.accept()

finally:
    browser.quit() 
