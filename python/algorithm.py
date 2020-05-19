#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import datetime


class CountTime(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def inner(self, *args):
            start_time = datetime.datetime.now()
            func()
            over_time = datetime.datetime.now()
            self.total_time = (over_time - start_time).total_seconds()
            return self.total_time
        return inner


class Algorithm(object):
    MAX_LEVEL = 20

    def __init__(self, func):
        self.func = func

        self.algorithm_standard_cfg = None

        self.start_time = time.time()
        self.end_time = 0
        self.total_time = 0
        self.total_space = 0

        self.test_data = None
        self.result_data = None
        self.answer_data = None

        self.data_score = 0
        self.time_score = 0
        self.space_score = 0
        self.total_score = 0
        self.max_score = 0

    def get_data_source(self, *args, **kwargs):
        """
        get the test source
        :return:
        """
        pass

    def get_real_answer_data(self, *args, **kwargs):
        """
        real answer algorithm function
        :return:
        """
        pass

    def exec_algorithm(self, *args, **kwargs):
        """
        exec you algorithm, then
        :return:
        """
        pass

    def get_algorithm_level(self, *args, **kwargs):
        """
        get the algorithm is level
        :return:
        """
        pass

    def test_level(self, *args, **kwargs):
        """
        :return:
        """
        pass

    def check_time(self, *args, **kwargs):
        pass

    def check_space(self, *args, **kwargs):
        pass

    def check_data(self, *args, **kwargs):
        pass

    def set_algorithm_standard(self, *args, **kwargs):
        """
        set the algorithm level standard data, like:
        [{
            "level": 1,
            "total_time": 100,
            "total_space": 1000,
            "data_len": 10
        }]
        and in function: get_algorithm_level to operation the data
        :return:
        """
        pass

    def finish(self, *args, **kwargs):
        """
        when algorithm finish, and reckon test score
        :return:
        """
        pass

    def reckon_test(self, *args, **kwargs):
        """
        reckon test score, include total time, total space, level
        :return:
        """
        pass

    def print_result(self, *args, **kwargs):
        """
        print result
        :return:
        """
        pass
