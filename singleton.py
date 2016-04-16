#!/usr/bin/env python


# 第一种方法__new__
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    """docstring for MyClass"""
    def __init__(self, *args, **kwargs):
        super(MyClass, self).__init__()
        pass


# 第二种方法 共享属性 __dict__
class Singleton1(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class MyClass1(object):
    """docstring for MyClass1"""
    def __init__(self, *arg, **kwargs):
        super(MyClass1, self).__init__()
        pass


# 第三种方法 装饰器
def singleton(cls, *args, **kwargs):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class MyClass2(object):
    """docstring for MyClass2"""
    def __init__(self, *args, **kwargs):
        super(MyClass2, self).__init__()
        pass


# 第四种方法，模块是天然的单例模式

# mysingleton.py
class MySingleton(object):
    def foo(self):
        pass


my_singleton = MySingleton()

# to use
from mysingleton import my_singelton


my_singleton.foo()
