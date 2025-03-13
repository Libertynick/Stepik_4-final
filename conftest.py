import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавляем обработку пользовательского аргумента --language
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: en, ru, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение языка из командной строки
    user_language = request.config.getoption("--language")

    print(f"\nstart browser with language {user_language} for test..")

    # Настройка ChromeOptions для установки языка браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Инициализация браузера с указанным языком
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")
    browser.quit()