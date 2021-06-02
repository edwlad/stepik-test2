import pytest
import time

links = [
    # следующий линк - это линк из задания
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/',
    # следующий линк - ошибка. Книги нет в продаже - значит нет кнопки добавить в корзину
    'http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/'
]


@pytest.mark.parametrize('link', links)
def test_find_add_to_basket_button(browser, link):
    browser.get(link)
    curr_language = browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
    find_buttons = browser.find_elements_by_css_selector("#add_to_basket_form .btn-add-to-basket")
    assert len(find_buttons) > 0, 'Не найдена кнопка добавления в корзину'
    assert len(find_buttons) < 2, 'Кнопка добавления в корзину не уникальна'
    if 'fr' in curr_language:
        time.sleep(30)