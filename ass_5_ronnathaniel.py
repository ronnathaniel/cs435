
from typing import List

"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 10/27/2021
Title: Programming Assignment #5
"""

# Problem 1
def one_distance_letter_diff(
    s: str,
    t: str,
) -> bool:
    """
    Check if two strings are one distance letter apart
    :param s: original string
    :param t: string post-distance letter operation
    :return: Bool determining if indeed one distance-letter apart
    """

    s_t  = len(s)
    t_t = len(t)

    is_one_diff = False

    # if the same length, check that ONLY one letter was changed
    # do that by flagging only if not already flagged
    # if attempting to flag a 2nd or 3rd time, don't allow.
    if s_t == t_t:
        for s_i, t_i in zip(s, t):
            if s_i != t_i:
                is_one_diff = True if not is_one_diff else False

    # if a letter was added/removed, len diff would be 1
    # we iterate since we want to remain agnostic as to which is the longer str
    # We should not care if s or t is longer, we simply try s - t & then t - s
    # if that failed.
    elif abs(s_t - t_t) == 1:
        s_s, t_s = set(s), set(t)

        pair = [s_s, t_s]

        # ONE-LINER of the exact same for-loop as below:
        # is_one_diff = any(map(lambda p: len(p[0] - p[1]) == 1, [pair, pair[::-1]] ))

        for _ in [pair, pair[::-1]]:
            # _ is guaranteed to have a __len__ of 2
            # it has to be either: [s_s, t_s]
            # or the reverse:      [t_s, s_s]
            # no need to check __len__.
            diff = _[0] - _[1]
            if not diff:
                continue
            elif len(diff) == 1:
                is_one_diff = True
                break

    return is_one_diff


# Problem 2
def is_anagram(
    s: str,
    t: str,
) -> bool:
    """
    Check if two strings are anagrams of the other.
    :param s: the first string to compare with
    :param t: the second string to compare with
    :return: Bool if the two strings are anagrams
    """

    # cannot simply compare unique letters as in a set
    # simply because: words might contain repeats of the same letter.
    # need to account for multiple intances of same letter in word.

    # counts is our mapping of chars to # of occurances
    counts = dict()

    # for s, we build up `counts`, adding up for each char occurance
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # for t, we break down `counts`, removing for each letter we find
    for char in t:
        if char in counts:
            if counts[char] > 1:
                counts[char] -= 1
            else:
                del counts[char]
        else:
            # if we are trying to remove a letter from counts which we
            # have not yet encountered, what this means is:
            # there is a letter in t, which does not exist in s.
            # We can already see these two are not anagrams.
            return False

    # if they are anagrams, `counts` should not be an empty dict.
    # if empty, we have proved anagrams.
    return not counts


# Problem 3
def insertion_index(
    nums: List[int],
    target: int,
) -> int:
    """
    Index or Insertion-Index of target in list of ints.
    Runs in O(log n) runtime.
    :param nums: list to check for target in
    :param target: item looking for
    :return: Index or Should-Be-Insertion Index of item in list
    """

    median_idx = len(nums) // 2
    median = nums[median_idx]
    not_found = False


    if median_idx < 1 and median != target:
        # We have already recursed all the way down
        # without findinf our target. Flag as not_found.
        not_found = True

    if target < median:
        if not_found:
            # in the case of target=4, and nums=[5], we suspect
            # the target should be at nums index=0, taking the place
            # of the 5 in nums. Inserted would look like: [4, 5].
            return median_idx
        # if still looking, repeat on the first half of nums
        return insertion_index(nums[:median_idx], target)
    elif target == median:
        # target found.
        return median_idx
    elif target > median:
        if not_found:
            # in the case of target=4, and nums=[3], we suspect
            # the target should be at nums index=1, taking the
            # spot after the 3. Inserted would resemble: [3, 4].
            return median_idx + 1
        # if still looking, repeat on the second half of nums
        # account for the offset by adding the indeces cut off in
        # the list slicing.
        return median_idx + insertion_index(nums[median_idx:], target)


if __name__ == '__main__':

    # PROBLEM 1 TESTS
    expected = True
    assert one_distance_letter_diff(**{
        's': 'ab',
        't': 'acb',
    }) == expected

    expected = False
    assert one_distance_letter_diff(**{
        's': '',
        't': '',
    }) == expected

    expected = True
    assert one_distance_letter_diff(**{
        's': '',
        't': 'A',
    }) == expected
    print('done problem 1 tests.')


    # PROBLEM 2 TESTS
    expected = True
    assert is_anagram(**{
        's': 'anagram',
        't': 'nagaram',
    }) == expected

    expected = False
    assert is_anagram(**{
        's': 'rat',
        't': 'car',
    }) == expected
    print('done problem 2 tests.')


    # PROBLEM 3 TESTS
    expected = 2
    assert insertion_index(**{
        'nums': [1, 3, 5, 6],
        'target': 5,
    }) == expected

    expected = 1
    assert insertion_index(**{
        'nums': [1, 3, 5, 6],
        'target': 2,
    }) == expected

    expected = 4
    assert insertion_index(**{
        'nums': [1, 3, 5, 6],
        'target': 7,
    }) == expected

    expected = 0
    assert insertion_index(**{
        'nums': [1, 3, 5, 6],
        'target': 0,
    }) == expected
    print('done problem 3 tests.')
    print('\ndone.')
