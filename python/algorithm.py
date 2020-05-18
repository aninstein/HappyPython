#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time


class Algorithm(object):
    MAX_LEVEL = 16

    def __init__(self, func):
        self.func = func

        self.algorithm_standard_cfg = None

        self.start_time = time.time()
        self.end_time = 0
        self.total_time = 0
        self.total_space = 0

        self.test_source_data = None
        self.exec_result_data = None
        self.real_answer_data = None

    def get_data_source(self, **kwargs):
        """
        get the test source
        :param data_len
        :return:
        """
        pass

    def get_real_answer_data(self):
        """
        real answer algorithm function
        :return:
        """
        pass

    def test_level(self, level=1):
        """
        :param level: 1-16
        :return:
        """
        pass

    def exec_algorithm(self):
        """
        exec you algorithm, then
        :return:
        """
        pass

    def get_algorithm_level(self):
        """
        get the algorithm is level
        :return:
        """
        pass

    def set_algorithm_standard(self):
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

    def finish(self):
        """
        when algorithm finish, and reckon test score
        :return:
        """
        pass

    def reckon_test(self):
        """
        reckon test score, include total time, total space, level
        :return:
        """
        pass

    def print_result(self):
        """
        print result
        :return:
        """
        pass
