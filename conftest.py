import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from selene import Browser, Config


@pytest.fixture(scope='function', autouse=True)
def driver_init():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'

    browser_config = Browser(Config(driver))

    yield browser_config

    attach.add_attachment(browser_config)
    attach.add_logs(browser_config)
    attach.add_html(browser_config)
    attach.add_video(browser_config)

    browser.quit()
