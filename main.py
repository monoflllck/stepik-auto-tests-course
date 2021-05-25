import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(url)


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    for fields in browser.find_elements(By.CSS_SELECTOR, ".form-group input"):
        fields.send_keys("abracadabra")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    send_file_form = browser.find_element(By.ID, "file")
    send_file_form.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    print_answer(browser)

finally:
    time.sleep(5)
    browser.quit()
