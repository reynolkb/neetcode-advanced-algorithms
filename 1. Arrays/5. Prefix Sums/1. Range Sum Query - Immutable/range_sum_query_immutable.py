from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sum_range(self, left: int, right: int) -> int:
        r = self.prefix[right]
        l = self.prefix[left - 1] if left > 0 else 0
        return r - l


def main():
    commands = ["NumArray", "sumRange", "sumRange", "sumRange"]
    values = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    output = []
    obj = None
    for i, command in enumerate(commands):
        if command == "NumArray":
            obj = NumArray(values[i][0])
            output.append(None)
        elif command == "sumRange":
            output.append(obj.sum_range(values[i][0], values[i][1]))
    print(output)


if __name__ == "__main__":
    main()
