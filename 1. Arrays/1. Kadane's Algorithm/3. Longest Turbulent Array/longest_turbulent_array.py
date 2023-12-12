from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Initialize two pointers: 'l' (left) and 'r' (right)
        l, r = 0, 1
        # Initialize 'res' to store the maximum turbulence size, and 'prev' to store the previous comparison sign
        res, prev = 1, ""

        # Iterate through the array until the right pointer reaches the end
        while r < len(arr):
            # Check if current pair forms a '>' pattern and it's not the same as the previous pattern
            if arr[r - 1] > arr[r] and prev != ">":
                # Update 'res' to the maximum of its current value and the current turbulence size
                res = max(res, r - l + 1)
                # Move the right pointer to the right
                r += 1
                # Set 'prev' to '>' indicating the last pattern
                prev = ">"

            # Check if current pair forms a '<' pattern and it's not the same as the previous pattern
            elif arr[r - 1] < arr[r] and prev != "<":
                # Update 'res' to the maximum of its current value and the current turbulence size
                res = max(res, r - l + 1)
                # Move the right pointer to the right
                r += 1
                # Set 'prev' to '<' indicating the last pattern
                prev = "<"

            # If neither '>' nor '<' pattern is formed
            else:
                # Move the right pointer to the right if the current and previous elements are equal
                r = r + 1 if arr[r] == arr[r - 1] else r
                # Reset the left pointer to one position left of the right pointer
                l = r - 1
                # Reset 'prev' as no consistent pattern is found
                prev = ""

        # Return the maximum turbulence size found
        return res


def main():
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    solution = Solution()
    result = solution.max_subarray_sum_circular(arr)
    print("Output:", result)


if __name__ == "__main__":
    main()
