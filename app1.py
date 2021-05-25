# import math
# from selenium.webdriver.common.by import By
# from selenium import webdriver


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))


# def print_answer(remote: webdriver.Remote):
#     alert = remote.switch_to.alert
#     print(alert.text.split()[-1])
#     alert.accept()


# browser = webdriver.Chrome()
# url = "http://suninjuly.github.io/get_attribute.html"
# browser.get(url)

# try:
#     x_element = browser.find_element(
#         By.ID, "treasure").get_attribute("valuex")
#     browser.find_element(By.ID, "answer").send_keys(calc(x_element))
#     elements_to_select = tuple(
#         ("[id='robotCheckbox']", "[id='robotsRule']", "button.btn-default"))

#     for elem in elements_to_select:
#         browser.find_element(By.CSS_SELECTOR, elem).click()
#     print_answer(browser)
# finally:  
#     browser.quit()  
