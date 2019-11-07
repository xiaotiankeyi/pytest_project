import os, sys
import os, sys
import pytest
from page.PostingPage import posting
from public.elementwait import findelement
from selenium.webdriver.common.by import By

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\page')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\public')

class Testposting():
    def test_case(self, browser, Login):
        result = Login
        print(result, type(result))
        if result == False:
            pytest.xfail('登录不成功,标记为失败')
        obj = posting(browser)
        el = obj.postnum.text
        obj.get("http://192.168.117.9:8080/jforum/jforum.page?module=posts&action=insert&forum_id=2")
        # pass

if __name__ == "__main__":
    pytest.main('-q', '-x')
