# coding=utf-8
# 加上第一行才能中文注释

mylist = ['item']
assert len(mylist) >= 1 # assert用来声明某个假设是真的，若假，则会引发一个AssertionError错误

mylist.pop()

assert len(mylist) >= 1