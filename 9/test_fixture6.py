#coding:utf-8


import pytest


@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    return a

@pytest.fixture()
def second(user):
    b = "abc1234"
    return (user,b)


def test_1(second):
    u = second[0]
    assert u == "yoyo"





if __name__ == "__main__":
    pytest.main(["-s", "test_fixture6.py"])