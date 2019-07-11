import pytest

"""
    目标：基于pytest实现参数化
    方法：@pytest.mark.parametrize("参数名",参数值)
    单个参数：
        键名：在一个字符串中
        值：为列表，如果多组数据，使用逗号分隔
"""


class Test02():
    @pytest.mark.parametrize("username",['admin001','admin002','admin003'])
    def test01(self, username):
        print("username:", username)
