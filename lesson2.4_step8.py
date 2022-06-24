from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))

    button1 = browser.find_element(By.ID, 'book')
    button1.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()

    print(browser.switch_to.alert.text)



finally:
    time.sleep(3)
    browser.quit()

    



