
from typing import List

"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 10/06/2021
Title: Programming Assignment #2
"""

# Problem 1
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
def find_target_terms(nums: List[int], target: int) -> List[int]:
    # iterating over copy of the list
    for i, first_t in enumerate(nums[ : ]):
        # compare against every other element in the list
        for j, second_t in enumerate(nums[ : ]):
            # skip if its the same element being looked at twice
            if i == j:
                continue
            # if the sum of our two, non-same elements is the target
            # then return our elements
            if first_t + second_t == target:
                return [i, j]
    # if nothing found, return -1 to signify failure
    return [-1, -1]

# Problem 2
# Given a string s, return the length of the longest substring that
# contains at most two distinct characters.
def longest_two_distinct_substring(s: str) -> int:
    longest_substr = 0
    # for every character in the string
    for i, start in enumerate(s[ : ]):
        substr = set(start)
        offset = i + 1
        # for every character following our current character
        # the use of a non-empty substr and offset to start allows
        # us to write a non-O(n**2) complexity, as we use only from
        # the following indices up. Now we can write in O(nlogn) complexity :-)
        for j, current in enumerate(s[offset : ]):
            # since j does not know of the location of i, we need
            # to match j with the current offsetted location
            j += offset
            # add our element to our
            substr.add(current)
            if len(substr) > 2:
                break
            current_substr = j - i + 1
            if current_substr > longest_substr:
                longest_substr = current_substr

    return longest_substr


if __name__ == '__main__':
    # Problem 1 Tests:
    nums = [2, 7, 11, 15]; target = 9; expected = [0, 1]
    assert find_target_terms(nums, target) == expected

    nums = [3, 2, 4]; target = 6; expected = [1, 2]
    assert find_target_terms(nums, target) == expected

    # Problem 2 Tests:
    s = "eceba"; expected = 3
    assert longest_two_distinct_substring(s) == expected

    s = "ccaabbb"; expected = 5
    assert longest_two_distinct_substring(s) == expected
