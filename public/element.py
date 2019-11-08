from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.select import Select

def elementwait(driver, way, obj):
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

def selectelement(el,value):
    """
    处理select下拉框元素
    :param el:
    :param value:
    :return:
    """
    Select(el).select_by_value(value=value)

def alertelement(driver, value, text=None):
    """
    alert警告跳窗处理
    :param driver:
    :return:
    """
    msg = driver.switch_to.alert.text
    if value == 'ok':
        driver.switch_to.alert.accept()
    elif value == 'on':
        driver.switch_to.alert.dismiss()
    if text is not None:
        driver.switch_to.alert.send_keys(text)
    return msg

def jselement(driver, width, height):
    """
    滚动条的操作
    :param driver: driver
    :param width: 宽
    :param height: 高
    :return:
    """
    js = "window.scrollTo({},{})".format(width, height)
    driver.execute_script(js)