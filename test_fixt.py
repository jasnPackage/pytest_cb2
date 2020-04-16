# coding:utf-8
import pytest
# 函数式


@pytest.fixture()
def login():
    print("输入账号，密码先登录")


def test_s1(login):
    print("用例1：登录之后其它动作111")


def test_s2():
    print("用例2：登录之后其它动作222")


def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_fixt.py"])