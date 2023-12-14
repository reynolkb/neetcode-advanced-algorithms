from typing import List


class Solution:
    @staticmethod
    def num_of_subarrays(arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cur_sum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            cur_sum += arr[L + k - 1]
            if (cur_sum / k) >= threshold:
                res += 1
            cur_sum -= arr[L]
        return res


def main():
    arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k = 3
    threshold = 5
    solution = Solution()
    result = solution.num_of_subarrays(arr, k, threshold)
    print("Output:", result)


if __name__ == "__main__":
    main()
