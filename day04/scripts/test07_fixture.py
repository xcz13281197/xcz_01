import pytest


# class Test01():
#     # 作用：将before变成 工厂函数
#     # 位置：在测试类中定义
#     @pytest.fixture()
#     def before(self):
#         print("before被执行")
#
#     def test01(self):
#         print("test01被执行")
#
#     # 通过参数 引用 工厂函数
#     def test02(self, before):
#         print("test02被执行")

# 作用：将before变成 工厂函数
# 位置：在测试类 外部
@pytest.fixture()
def before():
    print("before被执行")


class Test02():
    def test01(self):
        print("test01被执行")

    # 通过参数 引用 工厂函数
    def test02(self, before):
        print("test02被执行")
