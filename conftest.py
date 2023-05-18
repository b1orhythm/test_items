import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Enter language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lng = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        opt = Options()
        opt.add_experimental_option('prefs', {'intl.accept_languages': lng})
        browser = webdriver.Chrome(options=opt)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lng)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("\nstart chrome browser for test..")
        opt = Options()
        opt.add_experimental_option('prefs', {'intl.accept_languages': lng})
        browser = webdriver.Chrome(options=opt)
    yield browser
    print("\nquit browser..")
    browser.quit()
