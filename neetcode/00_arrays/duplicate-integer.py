from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False


sol = Solution()
cases = ([1, 2, 3, 3], [1, 2, 3, 4])

for case in cases:
    print(case)
    print(sol.hasDuplicate(case))
    print()
