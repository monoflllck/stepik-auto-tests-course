from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(url)

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    x = calc(x)

    input_value = browser.find_element(By.ID, "answer").send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert_text = alert.text
    print(alert_text)
    alert.accept()


finally:
    browser.quit()
