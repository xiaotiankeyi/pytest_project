from poium import PageElement, Page

class posting(Page):

    postnum = PageElement(xpath="//table[@cellpadding='2']/tbody/tr[4]/td[4]")