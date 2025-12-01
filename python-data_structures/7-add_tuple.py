#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    frst_a = 0
    frst_b = 0
    scnd_a = 0
    scnd_b = 0

    if len(tuple_a) == 1:
        frst_a = tuple_a[0]
        scnd_a = 0
    if len(tuple_a) == 0:
        frst_a, scnd_a = 0, 0
    if len(tuple_b) == 1:
        frst_b = tuple_b[0]
        scnd_b = 0
    if len(tuple_b) == 0:
        frst_b, scnd_b = 0, 0
    if len(tuple_a) >= 2:
        frst_a = tuple_a[0]
        scnd_a = tuple_a[1]
    if len(tuple_b) >= 2:
        frst_b = tuple_b[0]
        scnd_b = tuple_b[1]
    return (frst_a + frst_b, scnd_a + scnd_b)
