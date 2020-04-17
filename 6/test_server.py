#coding:utf-8

import pytest

@pytest.mark.webtest
def test_send_http():
    print("11")


def test_something_quick():
    print("22")


def test_another():
    print("33")


class TestClass():
    def test_method(self):
        print("44")


if __name__ == "__main__":
    pytest.main(["-s","test_server.py","-m='not webtest'"])