import pytest


@pytest.fixture(autouse=True)
def before():
    print("before被执行")


class Test02():
    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")
