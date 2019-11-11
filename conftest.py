import os, time
import pytest
from py._xmlgen import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + '\\report\\'

# 配置浏览器驱动
# driver_type = 'Chrome'
driver_type = 'chrome-headless'

# 配置运行的url
url = ""

# 失败重跑次数
failedRun = '2'

# 最大失败数
max_failedRun = '5'

# 配置运行测试目录
run_path = "./test_res/"


@pytest.fixture(scope='function')
def Login():
    """
    执行登录操作
    :return:
    """
    global driver
    driver.get("http://192.168.117.9:8080/jforum/user/login.page")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_css_selector('[type=submit]').click()
    try:
        assert driver.find_element_by_id('myprofile').text == '个人资料'
        return True
    except:
        return False
    pass


@pytest.fixture(scope='session')
def Loginout():
    """
    执行退出登录操作
    :return:
    """
    # global driver


@pytest.fixture(scope='function')
def base_url():
    global url
    return url


# 修改report.html中的Environment部分
def pytest_configure(config):
    config._metadata['测试地址'] = '193.168.117.9:8080'
    config._metadata['测试项目'] = 'BBS论坛系统'


# 修改Summary部分
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p('测试人员：赖志添')])
    prefix.extend([html.p('所属部门：测试部')])


# 设置用例描述表头
@pytest.mark.optionalhook
def pytest_html_results_tables_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()


# 设置用例描述表格
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"  # 获取截图

            capture_screenshot(file_name)  # 把截图存放进指定路径
            img_path = "image/" + file_name.split('/')[1]  # 存放进src里的路径
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def capture_screenshot(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    # global driver
    file_name = case_name.split("/")[-1]
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", file_name)
    driver.save_screenshot(image_dir)


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None


# 配置命令行参数
# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
#     )
#
# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")


# 启动配置的浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver

    if driver_type == 'Chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)

    elif driver_type == 'chrome-headless':
        chrome_options = Options()
        chrome_options.add_argument('- -headless')
        chrome_options.add_argument('- -disable-gpu')

        driver = webdriver.Chrome(chrome_options=chrome_options)

    else:
        raise NameError('driver驱动器定义错误')

    return driver


# 关闭浏览器
@pytest.fixture(scope='session', autouse=True)
def browser_close():
    yield driver
    time.sleep(20)
    driver.quit()
    print('test end。。。。')
