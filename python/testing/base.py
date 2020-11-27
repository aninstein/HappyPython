#!/usr/bin/env python
# -*- coding: utf-8 -*-

data_map = {}


def request_checker(module, function):
    def inner(cls):
        set_data_map(module, function, cls)
    return inner


def set_data_map(module, function, cls):
    if module not in data_map:
        data_map[module] = {}

    cls.module = module
    cls.function = function
    data_map[module][function] = cls


class Form(object):

    def __init__(self):
        print ">>>>>>>>>>>>>>>>> enter info Form __init__"
        self.function = "default"
        self.module = "default"

    def validate_req_data(self, data):
        print ">>>>>>>>>>>>>>>>> enter info Form validate_req_data"
        print self.function
        print self.module
        print data


@request_checker("subA", "subA_function")
class SubAForm(Form):
    @staticmethod
    def validate_param(data):
        print "validate_param A"


@request_checker("subB", "subB_function")
class SubBForm(Form):
    @staticmethod
    def validate_param(data):
        print "validate_param B"


def get_data_map(module, function):
    return data_map.get(module).get(function)
