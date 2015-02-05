#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

cache = {}

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    max_cycle = 0
    for x in range(i, j+1):
        cycle = 0
        if x in cache:
            cycle = cache[x]
        else:
            cycle = solver(x)
            cache[x] = cycle
        if (cycle > max_cycle):
            max_cycle = cycle

    return max_cycle

# ------
# solver
# ------
def solver (x):
    """
    Finds the cycle length of x
    Helper function for collatz_eval; does all the computation
    returns the cycle length of x
    """

    if (x == 0):
        return 0
    count = 1
    while( x != 1):
        if(x % 2 == 1):
            x = (3 * x) + 1
        else:
            x = x>>1
        count += 1
    return count

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)