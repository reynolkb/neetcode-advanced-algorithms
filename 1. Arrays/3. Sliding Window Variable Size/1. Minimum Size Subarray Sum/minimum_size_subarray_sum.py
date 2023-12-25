from typing import List


class Solution:
    @staticmethod
    def min_sub_array_len(target: int, nums: List[int]) -> int:
        res = float('inf')
        l, total = 0, 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float('inf') else 0


def main():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    solution = Solution()
    result = solution.min_sub_array_len(target, nums)
    print("Output:", result)


if __name__ == "__main__":
    main()
