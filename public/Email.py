import yagmail, os


def sendemail():
    '''查找最新的测试报告'''
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    report_dir = base_dir + '\\report'

    lists = os.listdir(report_dir)
    lists.sort(key=lambda lists: os.path.getmtime(report_dir + '\\' + lists))

    accept_report = find_report_dir(report_dir)  # 过的.html结尾的报告

    # 最终报告文件
    filename = os.path.join(report_dir, lists[-1], accept_report)
    print(filename)

    '''邮件定制'''
    obj = yagmail.SMTP(user='zhitian_lantuo@sina.com',
                       password='59c43837067936b5', host='smtp.sina.com')

    subject = "自动化测试报告"
    contents = "正文,请查看附件"

    """邮件发送"""
    obj.send(['laizhitian163@163.com', '1606291729@qq.com'],
             subject, contents, filename)


def find_report_dir(dir):
    try:
        # 查找最新的文件夹
        filelist = os.listdir(dir)
        filelist.sort()
        report_file = filelist[-1]
        result_dir = os.path.join(dir, report_file)

        # 查找以.html结尾的报告文件
        dir = os.listdir(result_dir)
        filelist = [i for i in dir if i.endswith('.html')]
        return filelist[0]
    except ImportError:
        return None


if __name__ == "__main__":
    sendemail()
