#coding:utf-8

import pytest

class Test():
    def test_one(self):
        pytest.skip(msg="跳过")
        assert 1==2


    def test_two(self):
        print("test_02")
        assert 1 == 1

if __name__ == "__main__":
    pytest.main(["-rs", "test_skip7.py"])