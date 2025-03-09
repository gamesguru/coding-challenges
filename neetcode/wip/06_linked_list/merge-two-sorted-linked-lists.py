from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        output = ListNode()

        while True:
            if list1.val < list2.val:
                output.next = ListNode(list1.val)

            if list1.next is None and list2.next is None:
                break

        return output


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test cases
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sol = Solution()

cases = [
    # My test cases
    # (),
    # NeetCode test cases
    ([1, 1, 2, 3, 4, 5], ([1, 2, 4], [1, 3, 5])),
    ([1, 2], ([], [1, 2])),
    ([], ([], [])),
]

# Run tests
for expected, _input in cases:
    print(_input)
    list1 = ListNode(_input[0][0])
    for i in range(1, len(_input[0])):
        list1.next = ListNode(_input[0][i])
    actual = sol.mergeTwoLists(_input[0], _input[1])
    print("assert {expected} == {actual}")
    print(f"assert {expected} == {actual}")
    print()
    assert expected == actual
