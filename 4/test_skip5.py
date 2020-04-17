#coding:utf-8

import pytest

@pytest.mark.skipif(1==2,reason='多个条件时，有1个条件满足就跳过(类)')
class Test():
    @pytest.mark.skipif(1==1,reason='多个条件时，有1个条件满足就跳过(方法)')
    def test_one(self):
        assert 1==2


    def test_two(self):
        print("test_02")
        assert 1 == 1

if __name__ == "__main__":
    pytest.main(["-rs","test_skip5.py"])