#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np

from python.algorithm import Algorithm


class SortTest(Algorithm):

    def __init__(self, func):
        super(SortTest, self).__init__(func)

    def get_data_source(self, low=1, high=10, data_len=10):
        self.test_source_data = np.random.randint(low, high, size=data_len)
        return self.test_source_data

    def get_real_answer_data(self):
        self.real_answer_data = sorted(self.test_source_data)
        return self.real_answer_data

    def set_algorithm_standard(self):
        cfg = []
        for i in range(1, self.MAX_LEVEL + 1):
            cfg.append({
                "level": i,
                "total_time": 100,
                "total_space": 1000,
                "data_len": pow(2, i) * 10
            })
        self.algorithm_standard_cfg = cfg







