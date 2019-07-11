import pytest
#autouse=True 开启自动运行
# #scope="class"  指定作用域为类级别
# @pytest.fixture(params=[1,2,3])
# def before(request):
#     # print("这是工厂函数")
#     return request.params

# @pytest.mark.usefixture("before")
class Test():
    # def setup_class(self):
    #     print("setup_class被执行")
    #
    # def setup(self):
    #     print("setup被执行")

    # def teardown(self):
    #     print("teardown被执行")

    # def teardown_class(self):
    #     print("teardown_class被执行")

    # @pytest.mark.run(order=2)
    def test01(self):
        print("test01被执行")
        #模拟失败
        # assert 0

    # @pytest.mark.run(order=1)
    def test02(self):
        print("test02被执行")

pytest.main("-s ./test02.py")


