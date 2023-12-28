class Solution:
    @staticmethod
    def character_replacement(s: str, k: int) -> int:
        count = {}

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            """
            current length of the window
            (r - l + 1)
            
            count of the most frequent character in the current window
            maxf 
            
            This calculates the number of characters in the current window that are not the most frequent character. 
            In other words, it's the count of characters that would need to be replaced to make the entire window 
            just one repeating character.
            (r - l + 1) - maxf
            
            This condition checks whether the number of characters that need to be replaced exceeds the allowed limit 
            'k'.
            (r - l + 1) - maxf > k
            """
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)


def main():
    s = "AABABBA"
    k = 1
    solution = Solution()
    result = solution.character_replacement(s, k)
    print("Output:", result)


if __name__ == "__main__":
    main()
