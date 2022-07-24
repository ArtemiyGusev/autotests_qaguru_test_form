import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def driver_init():
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()
