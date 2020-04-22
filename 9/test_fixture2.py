#coding:utf-8

import pytest

@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    b = "abc1234"
    return (a,b)


def test_1(user):
    u = user[0]
    p = user[1]
    assert u == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s","test_fixture2.py"])