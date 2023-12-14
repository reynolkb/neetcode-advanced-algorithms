# [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## Description

Given an array of integers `arr` and two integers `k` and `threshold`, return the number of sub-arrays of size `k` and
average greater than or equal to `threshold`.

Example 1:\
Input: `arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4`\
Output: `3`\
Explanation: `Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).`

Example 2:\
Input: `arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5`\
Output: `6`\
Explanation: `The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.`

## Run Command

`poetry run python "1. Arrays/2. Sliding Window Fixed Size/2. Number of Sub Arrays of Size K and Avg Greater than or Equal to Threshold/number_of_sub_arrays_of_size_k_and_avg_greater_than_or_equal_to_threshold.py"`