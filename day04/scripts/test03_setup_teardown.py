"""
    目标：特殊函数
        初始化
            函数：setup / teardown
            类级别：setup_class /teardown_class
        结束
"""
import pytest


class Test01():
    # 正确写法 函数级别
    # def setup(self):
    #     print("setup被执行")

    # 错误写法
    def setUp(self):
        print("setup被执行")

    # 正确写法 函数级别
    # def teardown(self):
    #     print("teardown被执行")

    # 错误写法 函数级别
    def tearDown(self):
        print("teardown被执行")

    # 定义测试方法
    def test_001(self):
        print("test001被执行")

    def test_002(self):
        print("test002被执行")


pytest.main("-s test03_setup_teardown.py")
