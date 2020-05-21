#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import operator

from algorithm import Algorithm, CountTime
from sort_algorithm.sort_function import bubble_sort, select_sort, insert_sort
from copy import deepcopy


class SortAlgorithm(Algorithm):

    def __init__(self, func):
        super(SortAlgorithm, self).__init__(func)
        self.set_algorithm_standard()
        self.temp_test_data = None

    def set_algorithm_standard(self):
        cfg = {}
        for i in range(1, self.MAX_LEVEL + 1):
            cfg[i] = {
                "level": i,
                "total_time": 5,  # S
                "total_space": 256,  # KB
                "low": 1,
                "high": int((i + 1) / 2) * 100,
                "data_len": pow(2, i) * 10
            }
        self.algorithm_standard_cfg = cfg
        self.max_score = self.MAX_LEVEL * 5
        self.time_max_score = self.MAX_LEVEL * 1
        self.space_max_score = self.MAX_LEVEL * 1

    def get_data_source(self, low=1, high=10, data_len=10):
        self.test_data = np.random.randint(low, high, size=data_len)
        self.test_data = list(self.test_data)
        self.get_real_answer_data()
        return self.test_data

    @CountTime()
    def get_real_answer_data(self):
        self.answer_data = list(sorted(self.test_data))
        self.answer_algorithm_time = self.total_time
        self.answer_algorithm_space = sys.getsizeof(self) / 1024
        return self.answer_data

    @CountTime()
    def exec_algorithm(self):
        self.result_data = self.func(self.temp_test_data)
        return self.result_data

    def get_algorithm_level(self):
        for i in range(1, self.MAX_LEVEL + 1):
            score = self.test_level(level=i)
            if score == 0:
                self.finish()
                break
            self.reckon_test()
        self.print_result()

    def test_level(self, level=1):
        value = self.algorithm_standard_cfg[level]
        self.get_data_source(low=value.get("low"),
                             high=value.get("high"),
                             data_len=value.get("data_len"))

        self.temp_test_data = deepcopy(self.test_data)
        self.exec_algorithm()
        if operator.eq(list(self.result_data), list(self.answer_data)):
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

    def reckon_test(self):
        self.level += 1
        self.data_percent = round(float(self.total_score / self.max_score), 3)
        self.time_percent = round(float(self.time_score / self.time_max_score), 3)
        self.space_percent = round(float(self.space_score / self.space_max_score), 3)

    def print_result(self):
        print(">>>>>>>>> algorithm result <<<<<<<<<")
        print("maximal test data: ", self.test_data)
        print("################################")
        print("last answer data: ", self.answer_data)
        print("last answer time: ", self.answer_algorithm_time)
        print("last answer space: ", self.answer_algorithm_space)
        print("################################")
        print("last result data: ", self.result_data)
        print("last total time: ", self.total_time)
        print("last total space: ", self.total_space)
        print("\n")
        print("*** result ***")
        print("*** algorithm right percent: {0}%".format(self.data_percent * 100))
        print("*** time right percent: {0}%".format(self.time_percent * 100))
        print("*** space right percent: {0}%".format(self.space_percent * 100))
        print("*** result, you algorithm level: %s ***" % self.level)
        print(">>>>>>>>>>>>>>>> end <<<<<<<<<<<<<<<<")


def sort_test_function(data):
    return sorted(data)


if __name__ == '__main__':
    ll = SortAlgorithm(bubble_sort)
    ll.get_algorithm_level()

