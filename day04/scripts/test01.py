import pytest
import unittest


class Test01(unittest.TestCase):
    # 定义测试方法
    def test_001(self):
        print("test001被执行")

    def test_002(self):
        print("test002被执行")

    def tess_003(self):
        print("test003被执行")


#
# print("我是普通方法")
# # 以普通方法运行
# Test01().test_001()
if __name__ == '__main__':
    print("条件成立!!！")
    pytest.main("-s test01.py")
else:
    print("条件不成立!!!")
