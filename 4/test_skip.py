#coding:utf-8

#skip跳过测试类

import pytest,sys

@pytest.mark.skip(reason="跳过Test类，会跳过类中所有方法")
class Test(object):
    def test_one(self):
        assert 1==1

    def test_two(self):
        print("test_02")
        assert 1==2

if __name__ == "__main__":
    pytest.main(["-rs","test_skip.py"])