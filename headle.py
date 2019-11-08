from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import re, random

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.get("http://192.168.117.9:8080/jforum/posts/list/27.page")

driver.get("http://192.168.117.9:8080/jforum/user/login.page")
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('admin')
driver.find_element_by_css_selector('[type=submit]').click()

driver.find_element_by_link_text('Python').click()

t = driver.find_elements_by_tag_name('a')
d = []
for i in t:
    z = re.findall('.*posts/list.*', i.get_attribute('href'))
    if not z:continue
    d.append(z)

a = random.randint(1, len(d))
driver.get(d[a][0])


driver.find_element_by_css_selector('.icon_topic_delete').click()

a = driver.switch_to.alert
# driver.switch_to.alert.accept()
a.accept()
print(a.text)

a = driver.window_handles
print(a)
# sleep(4)
# driver.quit()
#
# a = 'ADAD'
# if a is not None:
#     print('ss')
# else:
#     print('sds')