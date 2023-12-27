class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res


def main():
    s = "pwwkew"
    solution = Solution()
    result = solution.length_of_longest_substring(s)
    print("Output:", result)


if __name__ == "__main__":
    main()
