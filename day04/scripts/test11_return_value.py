import pytest

# autouse =True 开启自动运行
# scope = "class" 指定作用域为类级别
@pytest.fixture()
def before():
    # 返回值
    return 2


class Test02():
    def test01(self, before):
        print("工厂函数返回值：", before)
        print("test01被执行")

    def test02(self):
        print("test02被执行")

    def test03(self):
        print("test03被执行")
