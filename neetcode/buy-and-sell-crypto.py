from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test cases
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sol = Solution()

cases = [
    # My test cases
    (4, [9, 8, 2, 6, 1, 4]),
    # NeetCode test cases
    (6, [10, 1, 5, 6, 7, 1]),
    (0, [10, 8, 7, 5, 2]),
]

# Run tests
for expected, _input in cases:
    print(_input)
    actual = sol.maxProfit(_input)
    print("assert {expected} == {actual}")
    print(f"assert {expected} == {actual}")
    print()
    assert expected == actual
