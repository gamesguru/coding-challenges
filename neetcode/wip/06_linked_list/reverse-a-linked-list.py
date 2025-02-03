from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test cases
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sol = Solution()

cases = [
    # My test cases
    # (),
    # NeetCode test cases
    ([3, 2, 1, 0], [0, 1, 2, 3]),
    ([], []),
]

# Run tests
for expected, _input in cases:
    print(_input)
    actual = sol.reverseList(_input)
    print("assert {expected} == {actual}")
    print(f"assert {expected} == {actual}")
    print()
    assert expected == actual
