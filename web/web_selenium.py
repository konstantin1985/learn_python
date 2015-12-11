
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

browser = webdriver.Firefox()
browser.get('https://www.google.ru/')

try:
    assert 'Yandex' in browser.title
except WebDriverException as error:
    print 'error = ', error
    browser.close()
