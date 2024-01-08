from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sum_range(self, left: int, right: int) -> int:
        # You don't need to adjust self.prefix[right] because it already represents what you need, Teh total sum up
        # to and including the right element.
        r = self.prefix[right]
        # You subtract 1 from left because self.prefix[left] gives you the sum up to and including left. But you want
        # the sum of elements starting from left, so you need to subtract everything before it.
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
