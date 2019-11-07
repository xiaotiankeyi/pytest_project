from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

def findelement(driver, way, obj):
    """
    显示元素等待加元素判断
    :param driver:
    :param way:
    :param obj:
    :return:
    """
    try:
        ele = WebDriverWait(driver, 5, 0.5).until(ES.presence_of_element_located((way, obj)))
        return ele
    except:
        return False