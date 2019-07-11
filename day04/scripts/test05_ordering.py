import pytest

# 1. order值为正数，值越小优先级越高
# class Test01():
#     # 定义测试方法
#     @pytest.mark.run(order=3)
#     def test_001(self):
#         print("test001被执行")
#
#     @pytest.mark.run(order=1)
#     def test_002(self):
#         print("test002被执行")
#
#     @pytest.mark.run(order=2)
#     def test_003(self):
#         print("test003被执行")


# 2. order值为负数，值越小优先级越高
# class Test01():
#     # 定义测试方法
#     @pytest.mark.run(order=-3)
#     def test_001(self):
#         print("test001被执行")
#
#     @pytest.mark.run(order=-1)
#     def test_002(self):
#         print("test002被执行")
#
#     @pytest.mark.run(order=-2)
#     def test_003(self):
#         print("test003被执行")

# 3. order值为负数与正数同时存在,正数优先级高于负数
# class Test03():
#     # 定义测试方法
#     @pytest.mark.run(order=1)
#     def test_001(self):
#         print("test001被执行")
#
#     @pytest.mark.run(order=-1)
#     def test_002(self):
#         print("test002被执行")
#
#     @pytest.mark.run(order=-2)
#     def test_003(self):
#         print("test003被执行")

# 4. order值为标记正数与没有标记同时存在,被标记正数高于没有标记
# class Test04():
#     # 定义测试方法
#     # @pytest.mark.run(order=1)
#     def test_001(self):
#         print("test001被执行")
#
#     @pytest.mark.run(order=3)
#     def test_002(self):
#         print("test002被执行")
#
#     # @pytest.mark.run(order=-2)
#     def test_003(self):
#         print("test003被执行")

# 5. order值为标记负数与没有标记同时存在,没有被标记高于标记负数
class Test05():
    # 定义测试方法
    # @pytest.mark.run(order=1)
    def test_001(self):
        print("test001被执行")

    @pytest.mark.run(order=-3)
    def test_002(self):
        print("test002被执行")

    # @pytest.mark.run(order=-2)
    def test_003(self):
        print("test003被执行")