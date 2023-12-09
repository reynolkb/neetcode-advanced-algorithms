from typing import List


class Solution:
    @staticmethod
    def max_subarray_sum_circular(nums: List[int]) -> int:
        glob_max, glob_min = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0

        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            total += n
            glob_max = max(cur_max, glob_max)
            glob_min = min(cur_min, glob_min)

        # total --> all of the elements in the array
        # global_min --> minimum sum of subarray
        # total - global_min --> max sum when the sub_array wraps around
        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max


def main():
    nums = [5, -3, 5]
    solution = Solution()
    result = solution.max_subarray_sum_circular(nums)
    print("Output:", result)


if __name__ == "__main__":
    main()
