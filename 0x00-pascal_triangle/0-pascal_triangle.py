#!/usr/bin/python3
"""
pascals triagle assumes n will be always an integer

Return
    - a list of lists of integers representing the Pascal’s triangle of n
    - an empty list if n <= 0
"""


def pascal_triangle(n):
    'pascals triangle'
    final_list = [[1]]
    currnt_list = []
    append_list = [1]
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    for i in range(n-1):
        currnt_list.append(1)
        for i in range(len(append_list) - 1):
            currnt_list.append(append_list[i] + append_list[i + 1])
        currnt_list.append(1)
        final_list.append(currnt_list)
        append_list = currnt_list
        currnt_list = []
    return final_list
