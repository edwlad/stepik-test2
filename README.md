# Автотест для разных языков интерфейса

## Задание

[Описание задания на сайте](https://stepik.org/lesson/237240/step/9)  
Вам как разработчику автотестов нужно реализовать решение, которое позволит запускать автотесты для разных языков пользователей, передавая нужный язык в командной строке.  

1. Создайте GitHub-репозиторий, в котором будут лежать файлы [conftest.py](conftest.py) и [test_items.py](test_items.py).
1. Добавьте в файл `conftest.py` обработчик, который считывает из командной строки параметр **language**.
1. Реализуйте в файле `conftest.py` логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре **browser** и передаваться в тест как параметр.
1. В файл `test_items.py` напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по ссылке:  
<http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/>
1. Тест должен запускаться с параметром language следующей командой:  
`pytest --language=es test_items.py`  
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

## Что проверяется

1. Тест из репозитория можно запустить командой `pytest --language=es`, тест успешно проходит.
1. Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду `time.sleep(30)` сразу после открытия ссылки. Запустите тест с параметром `--language=fr` и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: **"Ajouter au panier"**.
1. Браузер должен объявляться в фикстуре **browser** и передаваться в тест как параметр.
1. В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы. **Есть assert**.
1. Название тестового метода внутри файла **test_items.py** соответствует задаче. Название *test_something* не удовлетворяет требованиям.

## Особенности реализации

1. Добавлено тестирование по ссылке:  
<http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/>  
На момент создания тестов, данный товар отсутствовал в продаже, следовательно нет кнопки добавления в корзину. Тест на этой ссылке "падает" с ошибкой.
1. Реализован запуск теста на разных браузерах: Chrome, Firefox, Edge. Каждому браузеру надо установить свой вебдрайвер. Для выбора используется параметр коммандной строки **browser_name**. Например:  
`pytest --browser_name=Firefox test_items.py`
1. Чтобы использовать Edge (Chromium) для тестирования в Selenium v3, необходимо установить модуль **msedge-selenium-tools**:  
`pip install msedge-selenium-tools`  
В `conftest.py` сделана проверка на наличе установленного модуля **msedge**.
1. При запуске теста с параметром `--language=fr`, будет пауза в выполнении на 30 секунд после открытия ссылки.
1. По умолчанию используются:
    - язык - `ru, en`
    - браузер - `Chrome`

## Для информации

### Параметры

Пример с параметрами:
`pytest -s -v --tb=line test_parser.py`

- `--tb=line` - чтобы сократить лог с результатами теста
- `-s` - выводить результат работы команды **print()**
- `-v` - подробная информация о прохождении тестов

### Перезапуск тестов

Установка:  
`pip install pytest-rerunfailures`  
Пример с перезапуском:  
`pytest --reruns 1 test_rerun.py`

- `--reruns 1` - один перезапуск

### Ошибка USB

Вариант исключения вывода в консоль ошибки USB **usb_device_handle_win.cc:...** в Windows 10 для Chrome ([источник](https://stackoverflow.com/questions/11613869/how-to-disable-logging-using-selenium-with-python-binding)):

```python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
```

### MS Edge и selenium v3

Добавить в проект средства selenium:  
`pip install msedge-selenium-tools`  
Чтобы запустить сеанс и автоматизировать Microsoft Edge (Chromium):

```python
from msedge.selenium_tools import Edge, EdgeOptions

# Launch Microsoft Edge (EdgeHTML)
driver = Edge()

# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options = options)
```

### Текущий язык браузера

Через запуск JS скрипта:

``` python
curr = driver.execute_script('return window.navigator.language || window.navigator.userLanguage')
```

### Разное

- `driver.execute_script('return window.navigator')` - данные о окне в браузере
- `driver.capabilities` - данные о браузере
