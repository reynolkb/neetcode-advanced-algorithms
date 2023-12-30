from typing import List


class Solution:
    @staticmethod
    def max_area(height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            container_height = min(height[l], height[r])
            container_width = r - l
            area = container_height * container_width
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1

        return res


def main():
    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 2, 1]
    solution = Solution()
    result = solution.max_area(height)
    print("Output:", result)


if __name__ == "__main__":
    main()
