#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def numbers(arr):
    if len(arr) == 1:
        return [arr]
    else:
        first = arr[0]
        perm = numbers(arr[1:])
        a = []
        for perms in perm:
            for i in range(len(perms)):
                tmp = perms[0:i] + [first] + perms[i:]
                a.append(tmp)
            a.append(perms + [first])
        return a


n = int(input("n = "))
print(numbers([i for i in range(1, n + 1)]))
