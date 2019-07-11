import pytest

"""
    目标：基于pytest实现参数化
    方法：@pytest.mark.parametrize("参数名",参数值)
    单个参数：
        键名：在一个字符串中
        值：为列表，如果多组数据，使用逗号分隔
    多个参数：
        键名：键名与键名必须放到一个字符串中（最容易犯错地方） 
              正确 如："name,age,pwd" 错误 如："name","age","pwd"
        值：为列表嵌套元祖
"""


class Test02():
    @pytest.mark.parametrize("username,password,verify_code",[("admin01","123456","8888"),("admin02","123457","8889")])
    def test01(self, username,password,verify_code):
        print("username:", username)
        print("password:", password)
        print("verify_code:", verify_code)
