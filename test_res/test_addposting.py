import random
import pytest
from page.addpostingpage import posting
from public.element import elementwait, selectelement, alertelement
from selenium.webdriver.common.by import By
from public.Logging import handle

logger = handle()
class Testposting():
    def test_case(self, browser, Login):
        """发帖子失败，没有填写主题"""
        result = Login
        logger.info('登录成功')
        obj = posting(browser)
        obj.python.click()  #点击python
        obj.subject.click()     #点击发表主题
        obj.choice_style.click()      #选择加粗

        selectelement(elementwait(obj.driver, By.NAME, 'addbbcode24'), 'red')    #调整字体颜色
        selectelement(elementwait(obj.driver, By.NAME, 'addbbcode26'), '18')    #调整字体为大

        data = ''.join(i for i in random.sample('njojsdfoffnfijonwnflw;sndfs nfuhnbrjbnjy97823njnsdjfs$#%$^@#%$$^&*^hkjfbadnjmnm', 40))
        obj.text_box.send_keys(data)    #输入发送内容
        obj.subject_type.click()    #选择发布主题类型
        logger.info('点击发送')
        obj.send_box.click()

        msg = alertelement(obj.driver)
        assert msg == '发表新主题必须要有文章标题'

    def test_case2(self, browser):
        """发帖子失败，没有添加内容"""
        logger.info('再次进行发送帖子测试，不添加内容发布')
        obj = posting(browser)

        titledata = ''.join(i for i in random.sample('njojsdfoffnfijonwnflwsndfsnfuhnbrjbnjy97823njnsdjfshkjfbadnjmnm', 20))
        obj.title_bar.send_keys(titledata)  #添加主题
        logger.info('清除先前留下的文本')
        obj.text_box.clear()    #清除文本输入框

        obj.subject_type.click()    #选择发布类型
        logger.info('点击发送')
        obj.send_box.click()

        msg = alertelement(obj.driver)
        assert msg == '发表文章必须要有文章内容'

    def test_case3(self, browser, Login):
        """发帖子成功"""
        logger.info('再次进行发送帖子测试，主题内容齐全')
        obj = posting(browser)
        obj.python.click()  #点击python
        obj.subject.click()     #点击发表主题
        obj.choice_style.click()      #选择加粗

        selectelement(elementwait(obj.driver, By.NAME, 'addbbcode24'), 'red')    #调整字体颜色
        selectelement(elementwait(obj.driver, By.NAME, 'addbbcode26'), '18')    #调整字体为大

        titledata = ''.join(i for i in random.sample('njojsdfoffnfijonwnflwsndfsnfuhnbrjbnjy97823njnsdjfshkjfbadnjmnm', 20))
        obj.title_bar.send_keys(titledata)    #输入标题

        textdata = ''.join(i for i in random.sample('njojsdfoffnfijonwnflsnfjnnjnj#%@#%^&*jbfjsamkw;sndfs nfuhnbrjbnjy97823njnsdjfs$#%$^@#%$$^&*^hkjfbadnjmnm', 40))
        obj.text_box.send_keys(textdata)  #写入文本
        obj.subject_type.click()
        logger.info('点击发送')
        obj.send_box.click()

        datemsg = elementwait(obj.driver, By.CSS_SELECTOR, ".date").text      #获取发布文章的时间
        msg = elementwait(obj.driver, By.XPATH, "//*[@class='subject']/a").text     #获取发布文章的主题
        assert msg == titledata
        logger.info('发布成功,文章主题为{},发布时间为{}'.format(msg, datemsg))

if __name__ == "__main__":
    pytest.main('-q', '-x')
