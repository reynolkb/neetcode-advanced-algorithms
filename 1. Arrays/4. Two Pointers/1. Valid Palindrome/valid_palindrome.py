class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])


def main():
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.is_palindrome(s)
    print("Output:", result)


if __name__ == "__main__":
    main()
