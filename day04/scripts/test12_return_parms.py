import pytest

# autouse =True 开启自动运行
# scope = "class" 指定作用域为类级别
# @pytest.fixture(params=[1,2,3])
@pytest.fixture(params="1")
def before(request):
    # 返回值
    return request.param


class Test02():
    def test01(self, before):
        print("工厂函数返回值：", before)
        print("test01被执行")

    def test02(self):
        print("test02被执行")

    def test03(self):
        print("test03被执行")
