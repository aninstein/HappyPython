#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


class CountTime(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def inner(*args):
            start_time = datetime.datetime.now()
            func_res = func(*args)
            end_time = datetime.datetime.now()
            total_time = end_time - start_time
            print "total time: ", total_time
            return func_res
        return inner
