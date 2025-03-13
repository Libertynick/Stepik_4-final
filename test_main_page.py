import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                         "https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1",
                         "https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1",
                         "https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])

def test_login(browser,links):
    link = f"{links}"
    browser.get(link)
    #log_locator = browser.find_element(By.XPATH, "//a[@id='ember463']")
    log = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='ember463']")))
    log.click()
    mail = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='login']")))
    mail.send_keys('libertynick@yandex.ru')
    password = browser.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("Nikitos12121994")
    button = browser.find_element(By.XPATH,"//button[@type='submit']")
    button.click()

    popup_locator = (By.XPATH, "//div[@id='ember533']")
    # Ожидание закрытия попапа
    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@class='navbar__profile-img']")))

    # vvod_locator = WebDriverWait(browser, 30).until(  # Увеличено время ожидания
    #     EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Введите ваш ответ здесь']"))
    # )

    #time.sleep(100)
    try:
        # Ждем элемент 15 секунд. Если элемент появится — кликнем
        element = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='again-btn white']"))
        )
        element.click()
    except TimeoutException:
        # Если элемент не найден — пропускаем
        print("Элемент не найден, продолжаем тест")

    vvod_locator = WebDriverWait(browser, 20).until(  # Увеличено время ожидания
        EC.element_to_be_clickable((By.XPATH, "//textarea[@required]"))
    )

    answer = str(math.log(int(time.time())))
    vvod_locator.send_keys(answer)

    button_sub = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='submit-submission']")))
    button_sub = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
    button_sub.click()

    # result = WebDriverWait(browser, 30).until(  # Увеличено время ожидания
    #     EC.presence_of_element_located((By.XPATH, "//p[@class='smart-hints__hint']"))
    # )
    incorrect_values = []
    try:
        elements = WebDriverWait(browser, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//p[@class='smart-hints__hint']"))
        )

        for element in elements:
            text = element.text.strip()
            if "Correct!" not in text:
                incorrect_values.append(text)
    except TimeoutException:
        incorrect_values.append("Элементы не найдены")

    print(incorrect_values)
 #text_to_be_present_in_element(By.XPATH, "//p[@class='smart-hints__hint']", text_)
