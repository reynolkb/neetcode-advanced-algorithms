from typing import List


class Solution:
    @staticmethod
    def subarray_sum(nums: List[int], k: int) -> int:
        # Initialize a counter for the number of subarrays that sum to k
        count = 0

        # Initialize a variable to keep track of the cumulative sum
        cur_sum = 0

        # Initialize a dictionary to store the frequency of cumulative sums
        # The dictionary starts with 0 mapped to 1 to handle cases where a subarray starts from the first element
        dic = {0: 1}

        # Iterate over each element in the nums array
        for i in range(len(nums)):
            # Add the current element to the cumulative sum
            cur_sum += nums[i]

            # Check if (cur_sum - k) is in the dictionary
            # It indicates the presence of a subarray ending at the current index which sums to k
            if cur_sum - k in dic:
                # Increment count by the number of times (cur_sum - k) has occurred
                count += dic[cur_sum - k]

            # Update the dictionary with the new cumulative sum
            # Increment the count of cur_sum in the dictionary, defaulting to 0 if not already present
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
