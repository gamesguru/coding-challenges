from typing import List
import heapq as hq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = self.nums
        hq.heapify(self.heap)

    def add(self, val: int) -> int:
        hq.heappush(self.heap, val)
        kth_largest_els = hq.nlargest(self.k, self.heap)
        return kth_largest_els[-1]


# [null,4,5,5,8,8]
_input = ["KthLargest", [3, [4, 5, 8, 2]], "add", [3], "add", [5], "add", [10], "add", [9], "add", [4]]

kth_largest = KthLargest(_input[1][0], _input[1][1])
for i in range(3, len(_input), 2):
    print(kth_largest.add(_input[i][0]))

print(kth_largest.heap)
