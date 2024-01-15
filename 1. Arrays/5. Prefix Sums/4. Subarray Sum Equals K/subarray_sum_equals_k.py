from typing import List


class Solution:
    @staticmethod
    def subarray_sum(nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        dic = {0: 1}
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in dic:
                count += dic[cur_sum - k]
            dic[cur_sum] = dic.get(cur_sum, 0) + 1
        return count


def main():
    nums = [1, 1, 1]
    k = 2
    solution = Solution()
    result = solution.subarray_sum(nums, k)
    print("Output:", result)


if __name__ == "__main__":
    main()
