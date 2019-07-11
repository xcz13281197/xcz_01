import pytest

# autouse =True 开启自动运行
# scope = "class" 指定作用域为类级别
@pytest.fixture(autouse=True, scope="class")
def before():
    print("before被执行")


class Test02():
    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")

    def test03(self):
        print("test03被执行")
