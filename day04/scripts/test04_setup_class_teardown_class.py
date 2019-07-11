"""
    目标：特殊函数
        初始化
            函数：setup / teardown
            类级别：setup_class /teardown_class
        结束
"""
import pytest


class Test01():
    # 类级别
    def setup_class(self):
        print("setup_class被执行")

    def teardown_class(self):
        print("teardown_class被执行")

    # 正确写法 函数级别
    def setup(self):
        print("setup被执行")

    # 正确写法 函数级别
    def teardown(self):
        print("teardown被执行")


    # 定义测试方法
    def test_001(self):
        print("test001被执行")

    def test_002(self):
        print("test002被执行")


pytest.main("-s test04_setup_class_teardown_class.py")
