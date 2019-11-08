from poium import PageElement, Page, PageElements

class delposting(Page):
    postnum = PageElement(xpath = "//table[@cellpadding='2']/tbody/tr[4]/td[4]")      #当前帖子数
    python = PageElement(link_text = 'Python')        #定位主页python
    tag_a = PageElements(tag='a')       #获取帖子的url
    del_box = PageElement(class_name='icon_topic_delete')       #定位删除按钮