# пример с параметрами:
# pytest -s -v --browser_name=firefox test_parser.py
#
# pip install pytest-rerunfailures - перезапуск тестов
# пример с перезапуском:
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
#  --reruns 1 - один перезапуск
#  --tb=line - чтобы сократить лог с результатами теста
#
# Вариант исключения ошибки USB: usb_device_handle_win.cc:1054 в Windows 10
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
#
# MS Edge and selenium v3
# pip install msedge-selenium-tools - добавить в проект средства selenium
# Чтобы запустить сеанс и автоматизировать Microsoft Edge (Chromium):
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options = options)
#
# driver.execute_script("return window.navigator.userLanguage || window.navigator.language")
# window.navigator - данные о странице в браузере
#
# driver.capabilities - данные о браузере


import pytest
import importlib.util
from selenium import webdriver

isedge = importlib.util.find_spec('msedge') is not None
if isedge:
    from msedge.selenium_tools import EdgeOptions, Edge


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='Chrome',  # или default=None,
        help='Choose browser: Chrome, Firefox, Edge'
    )
    parser.addoption(
        '--language',
        action='store',
        default='ru, en',  # или default=None,
        help='Language'
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name').capitalize()
    language = request.config.getoption('language')
    print(f'\nstart browser {browser_name} for test..')
    if browser_name == 'Firefox':
        options = webdriver.FirefoxProfile()
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(firefox_profile=options)
    elif isedge and browser_name == 'Edge':
        options = EdgeOptions()
        options.use_chromium = True
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = Edge(options=options)
    else:
        if browser_name != 'Chrome':
            print(f'\ndriver {browser_name} not found!')
            print('\nstart default browser Chrome for test..')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(5)

    yield driver

    print('\nquit browser..')
    driver.quit()
