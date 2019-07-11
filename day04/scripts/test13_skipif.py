import pytest

version = 2.0


class Test02():
    def test01(self):
        print("test01被执行")

    @pytest.mark.skipif(version == 2.0, reason="条件成立，被跳过！")
    # 没有原因直接跳过
    # @pytest.mark.skipif(reason="条件成立，被跳过！")
    # 注意：原因参数名不能为空；
    # @pytest.mark.skipif(2>1,"条件成立，被跳过！")
    def test02(self):
        print("test02被执行")

    def test03(self):
        print("test03被执行")
