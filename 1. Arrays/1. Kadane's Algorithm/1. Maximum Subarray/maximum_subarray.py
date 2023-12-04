from typing import List


class Solution(object):
    @staticmethod
    def max_sub_array(self, nums: List[int]) -> int:
        # default to first value of array
        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
            # if we have a negative prefix (numbers before), we remove it from our current sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sub


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    result = solution.max_sub_array(nums)
    print("Output:", result)


if __name__ == "__main__":
    main()
