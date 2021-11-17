
from typing import List, Any
import math

"""
Author: Ron Nathaniel
Course: CS 435: 101
Professor: Ionescu
Due: 11/10/2021
Title: Programming Assignment #7
"""

# Problem 1:
# Insert newInterval into intervals such that intervals is still sorted
# in ascending order by starti and intervals still does not have any
# overlapping intervals (merge overlapping intervals if necessary).
def insert_interval(intervals, new_interval):
    merged = []
    intervals = [*intervals, new_interval]
    intervals.sort(key = lambda inter: inter[0])
    # intervals includes the new interval, and is sorted based on start time

    for interval in intervals[:]:
        if (
            not merged
            or
            interval[0] > merged[-1][1]
        ):
            # non-conflicting merger of intervals
            merged.append(interval)
        if (
            merged[-1][1] < interval[1]
        ):
            # conflicting merger of intervals
            # extends interval into the longer period
            merged[-1][1] = interval[1]

    return merged


def sorted_median(nums1, nums2):
    merged = []
    while nums1 and nums2:
        # essentially a priority queue for nums1 and nums2
        # runs while both are not empty

        if nums1[0] < nums2[0]:
            smallest = nums1.pop(0)
        else:
            smallest = nums2.pop(0)
        merged.append(smallest)

    # after leaving the while loop, one list may still contain elems
    # therefore, we must add them all into the merged
    merged = [ *merged, *nums1, *nums2]
    merged_t = len(merged)

    if merged_t % 2 != 0:
        # if an uneven amount, we can simply take the middle element
        return merged[merged_t // 2]
    else:
        # if an even amount, we have to take the average of the middle and
        # the preceding element, since offset of indeces
        return (
            merged[merged_t // 2]
            +
            merged[merged_t // 2 - 1]
            ) / 2





if __name__ == '__main__':

    # PROBLEM 1 TESTS
    intervals = [[1,3],[6,9]]; new_interval = [2,5]
    expected = [[1,5],[6,9]]
    assert insert_interval(intervals, new_interval) == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]; new_interval = [4,8]
    expected = [[1,2],[3,10],[12,16]]
    assert insert_interval(intervals, new_interval) == expected

    intervals = []; new_interval = [5,7]
    expected = [[5,7]]
    assert insert_interval(intervals, new_interval) == expected

    intervals = [[1,5]]; new_interval = [2,7]
    expected = [[1,7]]
    assert insert_interval(intervals, new_interval) == expected


    # PROBLEM 2 TESTS
    nums1 = [1,3]; nums2 = [2]; expected = 2.00000
    assert sorted_median(nums1, nums2) == expected

    nums1 = [1,2]; nums2 = [3,4]; expected = 2.50000
    assert sorted_median(nums1, nums2) == expected

    nums1 = [0,0]; nums2 = [0,0]; expected = 0.00000
    assert sorted_median(nums1, nums2) == expected

    nums1 = [2]; nums2 = []; expected = 2.00000
    assert sorted_median(nums1, nums2) == expected
