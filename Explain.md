用例设计原则
    文件名以test_*.py文件和*_test.py
    以test_开头的函数
    以Test开头的类
    以test_开头的方法
    所有的包pakege必须要有__init__.py文件

执行用例规则
        pytest 文件名/
        pytest 脚本.py
    运行.py模块的下的某个函数
        pytest test_mod.py::test_func
    运行.py模块里面,测试类里面的某个方法
        pytest test_mod.py::TestClass::test_method
    
main([])运行参数
    -x 遇到错误停止测试,调式用
    - -maxfail = number     最大用例错误数,到达时就停止
    -q  简单显示测试信息
    - -reruns   用例失败重跑次数
    - -html = ./report/report.html
    - -self-contained-html  报告独立显示
    -s 关闭捕捉