import pytest

version = 2.0


class Test02():
    def test01(self):
        print("test01被执行")

    # @pytest.mark.xfail(2>1,reason="条件成立，标记预期失败！")
    @pytest.mark.xfail(reason="条件成立，标记预期失败！")
    def test02(self):
        print("test02被执行")

    def test03(self):
        print("test03被执行")
