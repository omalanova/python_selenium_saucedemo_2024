import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import LOGIN, PASSWORD, MAIN_PAGE

browser = webdriver.Chrome()

@pytest.fixture()
def browser():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1900,1000")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print('\nquit browser...')
    browser.quit()

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--window-size-1920, 1080")
    # service = Service(executable_path=ChromeDriverManager().install())
    # browser = webdriver.Chrome(service=service)
    # browser.maximize_window()
    # yield browser
    # print('\nquit browser...')
    # browser.quit()

@pytest.fixture()
def auth(browser):

    browser.get(MAIN_PAGE)
    browser.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    browser.find_element(*LOGIN_BUTTON).click()