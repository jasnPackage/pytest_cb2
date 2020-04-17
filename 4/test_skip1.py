#coding:utf-8

import pytest,sys

@pytest.mark.skipif(1==3,reason="跳过Test类，会跳过类中所有方法")
class Test():
    def test_one(self):
        assert 1==1

    def test_two(self):
        print("test_02")
        assert 1==2

if __name__ == "__main__":
    pytest.main(["-rs","test_skip1.py"])