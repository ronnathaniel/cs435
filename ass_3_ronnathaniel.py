from typing import List

"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 10/13/2021
Title: Programming Assignment #3
"""

# Problem 1:
# Given an integer array nums,
# move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def zero_reorder(
    nums: List[int]) -> List[int]:
    """
    Reorder all
    Assumption: elements found only in range(0, n).
    :param nums: list of positive integers and 0
    :return: mutated list with all 0's at end
    """
    for offset, num in enumerate(nums):
        if num:
            # we are only interested in the 0's.
            # any positive num will fail test.
            continue
        offse.t += 1
        for pos, _ in enumerate(nums[offset: ]):
            pos += offset
            nums[pos - 1], nums[pos] = nums[pos], nums[pos - 1]
    return nums


# Problem 2:
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
def missing_elem(
    nums: List[int]) -> int:
    """
    Finds the missing element in asc list.
    :param nums: list of numbers in a series
    :return: missing value in the series
    """
    n = len(nums) + 1
    for num in range(n):
        if num not in nums:
            return num
    return -1


if __name__ == '__main__':
    # PROBLEM 1 TESTS
    nums = [0,1,0,3,12]; expected = [1,3,12,0,0]
    assert zero_reorder(nums) == expected

    nums = [0]; expected = [0]
    assert zero_reorder(nums) == expected
    print('done P1 Tests.')

    # PROBLEM 2 TESTS
    nums = [3,0,1]; expected = 2
    assert missing_elem(nums) == expected

    nums = [9,6,4,2,3,5,7,0,1]; expected = 8
    assert missing_elem(nums) == expected
    print('done P2 Tests.')
