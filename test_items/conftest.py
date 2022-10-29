import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):  # задаём парсер, который будет считывать в КС язык с помощью параметра --language=
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language...")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstarting browser...")
    options = Options()
    options.add_experimental_option('prefs',         # даём браузеру понять, что надо принять язык пользователя
                                    {'intl.accept_languages': language}
                                    )
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nclosing browser...")
    browser.quit()



