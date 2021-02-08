#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/8 15:40
import pytest
def inc(x):
    return  x + 1
def test_answer():
    assert inc(3) == 5
class TestClass:
    def test_one(self):
        x = "hello"
        assert 'h' in x
    def test_two(self):
        x = "test"
        assert hasattr(x,'check')


# if __name__ == '__main__':
#     pytest("-s test_sample.py")
