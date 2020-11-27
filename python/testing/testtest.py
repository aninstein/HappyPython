#!/usr/bin/env python
# -*- coding: utf-8 -*-


import base
from base import get_data_map


if __name__ == '__main__':
    req_A_form = get_data_map("subA", "subA_function")
    print req_A_form
    req_A_form().validate_req_data("lichangan")

    req_B_form = get_data_map("subB", "subB_function")
    print req_B_form
    req_B_form().validate_req_data("zhuangruiying")
