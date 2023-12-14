from typing import List


class Solution:
    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            if k < right - left:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False


def main():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    solution = Solution()
    result = solution.contains_nearby_duplicate(nums, k)
    print("Output:", result)


if __name__ == "__main__":
    main()
