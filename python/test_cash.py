#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import time


# abs
def diff(data_hash, query_hash):
    data_hash2 = data_hash.copy()
    for item in range(len(data_hash2)):
        data_hash[item] = abs(data_hash[item] - query_hash[item])
    return data_hash


def addFlag(iter, query_hashes):
    for e in iter:
        yield (e[0], diff(e[1], query_hashes))


def createCombiner(x):
    list1 = [x]
    return list1


def mergeval(x, y):
    list1 = [y]
    list2 = x + list1
    return list2


def mergecomb(x, y):
    return x + y


def c2lsh(data_hashes, query_hashes, alpha_m, beta_n):
    start_time = time.time()
    print("start_time", start_time)
    offset = 0
    numCandidates = 0

    # data_hashes = data_hashes.map(lambda e : (e[0],diff(e[1], query_hashes)))
    data_hashes = data_hashes.mapPartitions(lambda e: addFlag(e, query_hashes))
    print("1. mapPartitions, time: ", time.time() - start_time)

    # data_hashes = data_hashes.map(lambda e: (e[1],e[0]))

    data_hashes = data_hashes.map(lambda e: (str(e[1]), e[0])).combineByKey(createCombiner, mergeval, mergecomb)
    print("2. combineByKey, time: ", time.time() - start_time)

    data_hashes = data_hashes.map(lambda e: (e[1], ast.literal_eval(e[0])))
    print("3. literal_eval, time: ", time.time() - start_time)

    first_time = 1
    candidatesRDD = []
    while_start = time.time()
    while_count = 0
    print("while_start", while_start)
    while numCandidates < beta_n:
        if offset == 0 and first_time == 1:
            first_time = 0
            continue
        else:
            offset = offset + 1
        # e : (id, difference)
        # zai map hou jia yiju zhege
        # data_hashes.cache()
        row_start = time.time()
        print("while count: %s, flatMap start time: %s" % (while_count, row_start))
        candidatesRDD = data_hashes.flatMap(
            lambda e: e[0] if ifQualified(e[1], len(e[1]), alpha_m, offset) == True else [])

        print("while count: %s, flatMap total time: %s" % (while_count, time.time() - row_start))
        numCandidates = candidatesRDD.count()
        print("while count: %s, flatMap total count time: %s" % (while_count, time.time() - row_start))

        print("offset: ", offset, "numCandidates: ", numCandidates)
        while_count += 1
    print("while_total_time", time.time() - while_start)
    return candidatesRDD


def ifQualified(difference, length, alpha_m, offset):
    count = 0
    for i in range(length):
        if difference[i] <= offset:
            count += 1
        if count >= alpha_m:
            return True
    return False

