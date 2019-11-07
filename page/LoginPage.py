from poium import PageElement,Page

class Loginelement(Page):

    """Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'."""
    username = PageElement(name='username')
    password = PageElement(name='password')
    logig = PageElement(css='[type=submit]')

    assert_succeed = PageElement(id_='myprofile')
    assert_failed = PageElement(css="font[color='red']")
