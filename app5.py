import math
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(url)

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    x = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()


finally:
    browser.quit()
