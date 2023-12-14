from typing import List


class Solution:
    @staticmethod
    def num_of_subarrays(self, arr: List[int], k: int, threshold: int) -> int:
        print("Hello World")


def main():
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    solution = Solution()
    result = solution.num_of_subarrays(arr, k, threshold)
    print("Output:", result)


if __name__ == "__main__":
    main()
