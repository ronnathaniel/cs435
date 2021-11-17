
from typing import List

"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 11/17/2021
Title: Programming Assignment #8
"""

# Problem 1:
# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
def next_time(t: str) -> str:
    """
    :param t: timestring of current time
    :return: timestring of next time resuing the same digits
    """
    def get_hour(_t: str):
        return int(_t.split(':')[0])

    def get_minute(_t: str):
        return int(_t.split(':')[1])

    def get_uniq_digits(_t: str):
        digits = [char for char in _t if char.isdigit()]
        return set(digits)

    t_uniq = get_uniq_digits(t)
    time_m = get_hour(t) * 60 + get_minute(t)

    for _ in range(time_m + 1, time_m + 60 * 24, 1):
        offset = _ % (60 * 24)
        _h = offset // 60
        _m = offset % 60

        t_new = '{h:02d}:{m:02d}'.format(h=_h, m=_m)
        t_new_uniq = get_uniq_digits(t_new)

        if all([d in t_uniq for d in t_new_uniq]):
            return t_new
        else:
            continue


# Problem 2:
# Given n pairs of parentheses,
# write a function to generate all combinations of well-formed parentheses.
def paran_combos(n: int, curr: str = None, parans = None, left_used: int = 0, right_used: int = 0) -> List[str]:
    """
    :param n: pairs of parans to create
    :param curr: current working parans combo
    :param parans: list of all known combos
    :param left_used: amount of left parans used
    :param right_used: amount of right parans used
    :return: list of parans evenly balanced with n opens and n closes
    """

    if parans is None:
        parans = []
    curr = curr or ''

    found = [used == n  for used in [left_used, right_used]]

    if all(found):
        parans.append(curr)
    else:
        if left_used < n:
            paran_combos(n, curr + '(', parans, left_used + 1, right_used)
        if right_used < left_used:
            paran_combos(n, curr + ')', parans, left_used, right_used + 1)
    return list(set(parans))



if __name__ == '__main__':
    # Problem 1 Tests
    time = "19:34"; expected = "19:39"
    assert next_time(time) == expected

    time = "23:59"; expected = "22:22"
    assert next_time(time) == expected

    # Problem 2 Tests
    n = 3; expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert all(combo in expected for combo in paran_combos(n))

    n = 1; expected = ['()']
    assert set(paran_combos(n)) == set(expected)
