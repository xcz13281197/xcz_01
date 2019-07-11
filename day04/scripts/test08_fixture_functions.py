import pytest

# 作用：将before变成 工厂函数
# 位置：在测试类 外部
@pytest.fixture()
def before():
    print("before被执行")


# 通过函数方式，来修饰类-->类中所有测试开头的方法，运行之前都会被执行
@pytest.mark.usefixtures("before")
class Test02():
    def test01(self):
        print("test01被执行")

    # 通过函数 引用 工厂函数
    # @pytest.mark.usefixtures("before")
    def test02(self):
        print("test02被执行")
