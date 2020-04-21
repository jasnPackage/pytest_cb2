#coding:utf-8

import pytest

#测试登录数据
test_user_data = ["admin1","admin2"]


@pytest.fixture(scope="module")
def login_func(request):
    '''普通登录函数'''
    user = request.param
    print("登录账户：%s"%user)
    return user


@pytest.mark.parametrize("login_func",test_user_data,indirect=True)
def test_login(login_func):
    '''登录用例'''
    a = login_func
    print("测试用例中login的返回值：%s" %a)
    assert a != ""


if __name__ == "__main__":
    pytest.main(["-s","test_02.py"])