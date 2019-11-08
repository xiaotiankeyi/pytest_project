from poium import PageElement, Page

class posting(Page):

    """Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'."""

    postnum = PageElement(xpath = "//table[@cellpadding='2']/tbody/tr[4]/td[4]")      #当前帖子数
    python = PageElement(link_text = 'Python')        #定位主页python
    subject = PageElement(class_name = 'icon_new_topic' )   #定位发表主题
    choice_style =  PageElement(css= "input[name='addbbcode0']")      #定位加粗
    text_box = PageElement(class_name = 'message')      #定位文本输入框
    subject_type = PageElement(id_= 'topic_type1')      #定位置顶
    send_box = PageElement(id_= 'btnSubmit')    #定位发送
    title_bar = PageElement(name='subject')     #定位标题栏
