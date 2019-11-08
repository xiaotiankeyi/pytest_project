from page.delpostingpage import delposting
import pytest, re, random
from page.addpostingpage import posting
from public.element import elementwait, selectelement, alertelement
from selenium.webdriver.common.by import By
from public.Logging import handle

class Testdelposting():
    def test_case(self, browser, Login):
        obj = delposting(browser)
        num = obj.postnum.text
        obj.python.click()

        ele = obj.tag_a     #获取帖子的url
        posting_url = []
        for i in ele:
            z = re.findall('.*posts/list.*', i.get_attribute('href'))
            if not z:continue
            posting_url.append(z)
        a = random.randint(1, len(posting_url))
        obj.get(posting_url[a][0])      #随机进去一篇帖子
        obj.del_box.click()
        alertelement(obj.driver, value='ok', text='hsfhasfjsafa')

if __name__ == "__main__":
    pass