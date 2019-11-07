import os
import time
import pytest
import click
from conftest import run_path, REPORT_DIR, max_failedRun, failedRun


def creart_dir(now_time):
    """
    创建存放测试报告及存放图片的目录
    :param now_time:
    :return:
    """
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + '/image')


@click.command()
@click.option('-m', default=None, help='输入运行模式：run或debug')
def run(m):
    if m is None or m == 'run':
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        creart_dir(now_time)

        html_report = os.path.join(REPORT_DIR, now_time, 'htmlResult.html')
        xml_report = os.path.join(REPORT_DIR, now_time, 'Result-xml.xml')

        pytest.main(['-s', '-q', run_path,
                     '--html=' + html_report,
                     '--junit-xml=' + xml_report,
                     '--self-contained-html',
                     '--maxfail', max_failedRun,
                     '--reruns', failedRun])
    elif m == 'debug':
        print('debug调式模式,开始执行,,,,')
        pytest.main(['-v', '-s', run_path])
        print('运行结束....')


if __name__ == "__main__":
    run()
