from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        print("hello world")


def main():
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    solution = Solution()
    result = solution.max_subarray_sum_circular(arr)
    print("Output:", result)


if __name__ == "__main__":
    main()
