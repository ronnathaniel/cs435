
from typing import List

"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 10/20/2021
Title: Programming Assignment #4
"""


# Problem 3
# Given a string s and an integer k, return the length
# of the longest substring of s that contains at most k distinct characters.
def longest_dist_substr(s: str, k: int) -> int:
    """
    :param s: string to find largest distinct substring
    :param k: number of most distinct chars in substring
    :return: length of largest distinct substring
    """

    def _num_dist_letters(_s: str) -> int:
        """
        Helper function to show number of distinct chars in string
        sets {} are comprised of unique (aka distinct), and len()
        shows the size.
        """
        return len(set(_s))

    longest = ''
    for i, _ in enumerate(s[ : ]):
        for j, _ in enumerate(s[i : ]):
            j += i + 1
            current = s[i : j]

            # IF we have too many distinct, DISCARD
            if _num_dist_letters(current) > k:
                break

            # IF our current is longer than what we already know
            # MAKE this current the longest
            if len(current) > len(longest):
                longest = current
    return len(longest)


# Problem 4
def peak_index(nums: List[int]) -> int:
    """
    Finds the index of a Peak Elem.
    Chosen to stop at the first peak element.
    :param nums: list of nums to find peak elem
    :return: index of first peak element. -1 if not found.
    """
    for i, num in enumerate(nums[ : ]):
        # IF we cannot do i - 1 or i + 1, DISCARD
        if not i or i == len(nums) - 1:
            continue
        # ELSE IF current index is larger than i - 1 and i + 1, RETURN
        elif (
            num > nums[i - 1]
        and
            num > nums[i + 1]
        ):
            return i

    # RETURN -1 to show failure
    return -1


if __name__ == '__main__':

    # Problem 3 Tests
    s = 'eceba'; k = 2; expected = 3
    assert longest_dist_substr(s, k) == expected

    s = 'aa'; k = 1; expected = 2
    assert longest_dist_substr(s, k) == expected

    # Problem 4 Tests
    nums = [1,2,3,1]; expected = 2
    assert peak_index(nums) == expected

    nums = [1,2,1,3,5,6,4]; expected = [1, 5]
    assert peak_index(nums) in expected
