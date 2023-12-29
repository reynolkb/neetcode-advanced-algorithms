from typing import List


class Solution:
    @staticmethod
    def two_sum(numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


def main():
    numbers = [3, 24, 50, 79, 88, 150, 345]
    target = 200
    solution = Solution()
    result = solution.two_sum(numbers, target)
    print("Output:", result)


if __name__ == "__main__":
    main()
