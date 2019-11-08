import pytest
from page.loginpage import Loginelement
from public.element import elementwait
from selenium.webdriver.common.by import By
from public.Logging import handle

logger = handle()


@pytest.mark.Login
class TestLogin():

    @pytest.mark.parametrize(
        "username, password",
        [('admin', 'admin'),
         ('adminjksdas', 'admin'),
         ('admin', '123456')
         ],
        ids=['登录成功', '用户名正确密码错误失败', '用户名错误密码正确失败']
    )
    def test_case(self, browser, username, password):
        obj = Loginelement(browser)
        obj.get("http://192.168.117.9:8080/jforum/user/login.page")

        obj.username.send_keys(username)
        obj.password.send_keys(password)
        obj.logig.click()
        logger.info('{}开始登录，，，'.format(username))
        if username == 'admin':
            assert obj.assert_succeed.text == '个人资料'
        else:
            assert '无效的用户名或错误' in obj.assert_failed.text


if __name__ == "__main__":
    pytest.main(['-q, -x', ])
