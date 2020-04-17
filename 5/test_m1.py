#coding:utf-8

import pytest
from test_caseskip import myskip

class Test():
    @myskip
    def test_one(self):
        print("test_one方法执行")
        assert 1 == 1


    def test_two(self):
        print("test_two方法执行")
        assert 'o' in 'love'


if __name__ == "__main__":
    pytest.main(["-rs", "test_m1.py"])
