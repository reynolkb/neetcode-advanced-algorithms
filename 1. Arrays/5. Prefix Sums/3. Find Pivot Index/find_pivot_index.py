from typing import List


class Solution:
    @staticmethod
    def pivot_index(nums: List[int]) -> int:
        total = sum(nums)

        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


def main():
    nums = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    result = solution.pivot_index(nums)
    print("Output:", result)


if __name__ == "__main__":
    main()
