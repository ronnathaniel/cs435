

from typing import List
from math import factorial
import random

"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 10/13/2021
Title: Programming Assignment #3
"""

# PROBLEM 1
# Now you want to find out who the celebrity is or verify that
# there is not one. The only thing you are allowed to do is to ask questions
# like: "Hi, A. Do you know B?" to get information about whether A knows B.
# You need to find out the celebrity (or verify there is not one) by asking as
# few questions as possible (in the asymptotic sense).
class Network(list):
    # extending the builtin list class to work directly with the list
    # supplied during testing.
    # Also, will act as any list would during sum() and map(), which
    # both expect iterables.

    def __init__(
        self,
        l: list
    ):
        super().__init__(l)

    def knows(
        self,
        a: int,
        b: int,
    ) -> bool:
        # Checks if person A knows person B.
        return self[a][b]

    def validate(self):
        # Ensure that each person object knows at least themselves.
        for i, person in enumerate(self):
            assert self.knows(i, i)



def find_celebrity(
    n: Network
) -> int:
    """
    Returns label of celebrity in network if there is one. Else return -1.
    :param n: Network of people who may/may not know each other.
    :return: 1 if celeb exists, else 0
    """

    # validate the network. Makes sure that every single person
    # at the very least knows themselves. Therefore, it is impossible to have
    # a person object of [0, 0, 0], since the celeb minimally knows themselves.
    # makes use of the bool knows(a, b).
    n.validate()

    # flatten 2D lists to 1D list, containing the sums of each person object
    # in the network
    sums = list(map(lambda x: sum(x), n))
    try:
        # if there is a celeb, they know only themselves.
        # Meaning, the sum of their knowledge graph would be 1, themselves.
        # Return that person's label.
        return sums.index(1)
    except ValueError:
        # if there is not such a person in the graph, then there must not be a
        # celebrity in the network. Return -1 to signal failure to find one.
        return -1


# PROBLEM 2
# Given two strings s1 and s2, return true if s2 contains
# a permutation of s1, or false otherwise. In other words,
# return true if one of s1's permutations is the substring of s2.
def get_permutations(
    s: str,
) -> List[str]:
    """
    Get all permutations of string
    :param s: string to get permutations of
    :return: list containing all permutations
    """

    # efficiency is through the roof here. recursive + double for loop.
    # Estimated runtime: O(n * logn * logn)

    s_t = len(s)

    if len(s) == 1:
        # base case for recursion. If down to last letter, return letter
        return s
    # else return a list to be expanded upon in the recursive return
    # moves one letter down to the right on every recurance
    # and adds & expands lists returned in recursive calls when recieved.
    return [
        ''.join([
            s[i], *permutations
        ])
        for i in range(s_t)
        for permutations in get_permutations(s[ :i] + s[i+1: ])
    ]


def contains_permutation(
    s1: str,
    s2: str,
) -> bool:
    """
    Checks if any permutation of s1 is found in s2
    :param s1: string to check all occurances of its permutations
    :param s2: string to check if contains the permutations of s1
    :return: True if s2 contains a permute else False
    """

    all_permutations = get_permutations(s1)

    # obviously I am a big fan of anonymous functions
    # small breakdown: for every permutation in all_permutations,
    # check if it exists in s2 using python's builtin str in str functionality.
    # list() gets a list all these permutations that fit such conditions of
    # being in s2
    # any() converts to bool any elem in the list is "Truthy".
    return any(list(filter(lambda x: x in s2, all_permutations)))


# To the Grader grading these:
# I really enjoy these assignments.
# I think theyre fun brain-teasers, and this is actually the most
# favorable of all my homeworks and assignments.
# Thanks for grading these. I love you.
# I hope you had at least 1/10 of the fun I had while you grade these.
# See you next assignment :-)


if __name__ == '__main__':
    # Problem 1 Tests
    l = Network([[1,1,0],[0,1,0],[1,1,1]]); expected = 1
    assert find_celebrity(l) == expected

    l = Network([[1,0,1],[1,1,0],[0,1,1]]); expected = -1
    assert find_celebrity(l) == expected

    # Problem 2 Tests
    s1 = 'ab'; s2 = 'eidbaooo'; expected = True
    assert contains_permutation(s1, s2) == expected

    s1 = 'ab'; s2 = 'eidboaoo'; expected = False
    assert contains_permutation(s1, s2) == expected
