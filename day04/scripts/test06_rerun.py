import pytest


class Test01():
    # 定义测试方法
    def test_001(self):
        print("test001被执行")

    def test_002(self):
        print("test002被执行")
        # 模拟失败
        # assert False
        assert 0

    def test_003(self):
        print("test003被执行")
