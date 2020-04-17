#coding:utf-8

import pytest

class Test():
    @pytest.mark.skip(reason='跳过一个方法或一个测试用例')
    def test_one(self):
        assert 1==2


    def test_two(self):
        print("test_02")
        assert 1 == 1

if __name__ == "__main__":
    pytest.main(["-rs","test_skip3.py"])