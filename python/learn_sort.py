#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import operator

from python.algorithm import Algorithm, CountTime


class SortTest(Algorithm):

    def __init__(self, func):
        super(SortTest, self).__init__(func)

    def set_algorithm_standard(self):
        cfg = {}
        for i in range(1, self.MAX_LEVEL + 1):
            cfg[i] = {
                "level": i,
                "total_time": 100,  # S
                "total_space": 1024,  # KB
                "low": 1,
                "high": int(i / 2) * 100,
                "data_len": pow(2, i) * 10
            }
        self.algorithm_standard_cfg = cfg
        self.max_score = self.MAX_LEVEL * 5

    def get_data_source(self, low=1, high=10, data_len=10):
        self.test_data = np.random.randint(low, high, size=data_len)
        return self.test_data

    def get_real_answer_data(self):
        self.answer_data = sorted(self.test_data)
        return self.answer_data

    @CountTime()
    def exec_algorithm(self):
        self.result_data = self.func(self.test_data)
        return self.result_data

    def get_algorithm_level(self):
        pass

    def test_level(self, level=1):
        value = self.algorithm_standard_cfg[level]
        self.get_data_source(low=value.get("low"),
                             high=value.get("high"),
                             data_len=value.get("data_len"))

        self.exec_algorithm()

        if operator.eq(self.result_data, self.answer_data):
            self.data_score += 3
        else:
            self.data_score = self.check_data(self.result_data, self.answer_data)

        if self.data_score == 0:
            return 0

        self.total_space = sys.getsizeof(self) / 1024
        if self.total_space <= value.get("total_space"):
            self.space_score += 1

        if self.total_time <= value.get("total_time"):
            self.time_score += 1

        self.total_score = self.data_score + self.time_score + self.space_score
        return self.total_score

    def check_data(self, result, answer):
        if len(result) != len(answer):
            return 0
        data_len = len(result)
        for i in range(data_len):
            if result[i] == answer[i]:
                continue

            if i <= data_len * (1 / 3):
                return 0
            elif i <= data_len * (2 / 3):
                return 1
            elif i <= data_len:
                return 2
        else:
            return 3

