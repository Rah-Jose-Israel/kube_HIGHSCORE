import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def start_game(BUTTONS) -> bool:
    for button in BUTTONS:
        clickable = button.find_element(
            By.TAG_NAME, "button")
        if clickable:
            clickable.click()
            return True


def get_box_spans(box_element: list) -> list:
    for element in box_element:
        return element.find_elements(
            By.CSS_SELECTOR, "span[style]")


def corrected_background_color_selection(spans: list) -> str:
    style_list = []
    for span_element in spans:
        style_list.append(span_element.get_attribute("style"))
    return list(set(style_list) - set([x for x in style_list if style_list.count(x) > 1]))[0]


def print_score_time(driver_) -> None:
    for em in driver_.find_elements(By.TAG_NAME, "em"):
        score = em.text
    time = driver_.find_element(By.CLASS_NAME, "time").text
    print(f"Score: {score} TIME LEFT: {time}")


"""OBTAIN DRIVERS"""
print("CHROME_DRIVER")
DRIVER = webdriver.Chrome()
DRIVER.get("https://kuku-kube.com/")
DRIVER.set_window_position(500, 0)

''''''''''''''''''''''''''''''''''''

"""Starting GAME"""
START_KUKU_KUBE = start_game(
    BUTTONS=DRIVER.find_elements(
        By.CLASS_NAME, "btns"))
''''''''''''''''''''''''
while True:
    """Entering the game room """
    if START_KUKU_KUBE:
        GAME_BOX_ELEMENT = DRIVER.find_elements(
            By.ID, "box")
        GAIN_SPAN_BACKGROUND_COLOR = get_box_spans(
            box_element=GAME_BOX_ELEMENT)
        GET_UNIQUE_SPAN = corrected_background_color_selection(
            spans=GAIN_SPAN_BACKGROUND_COLOR)
        AUTO_CLICK = DRIVER.find_element(
            By.CSS_SELECTOR, f"span[style='{GET_UNIQUE_SPAN}']").click()
        CARD = print_score_time(
            driver_=DRIVER)
