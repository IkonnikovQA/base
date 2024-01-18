from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_base():
    browser = webdriver.Chrome()
    browser.get('https://www.qa-practice.com/elements/button/simple')
    browser.find_element(By.ID, 'submit-id-submit').click()
#TEXT
   #browser.find_element(By.LINK_TEXT, 'Contact').click()
#CSS
    #browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]').click()
#XPATH
    #browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]').click()