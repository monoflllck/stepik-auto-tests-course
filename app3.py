import math
import time
from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome()
url = "https://SunInJuly.github.io/execute_script.html"
browser.get(url)

try:
    x = int(browser.find_element(By.ID, "input_value").text)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)

    for select in ['#robotCheckbox', '#robotsRule', 'button.btn']:
        browser.find_element(By.CSS_SELECTOR, select).click()

    # robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    # browser.execute_script(
    #     'return arguments[0].scrollIntoView(true);', robot_checkbox)
    # robot_checkbox.click()

    # robots_rule = browser.find_element(By.ID, "robotsRule")
    # browser.execute_script(
    #     "return arguments[0].scrollIntoView(true);", robots_rule)
    # robots_rule.click()

    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # browser.execute_script(
    #     "return arguments[0].scrollIntoView(true);", button)
    # button.click()

    print_answer(browser)
finally:
    time.sleep(3)
    browser.quit()
