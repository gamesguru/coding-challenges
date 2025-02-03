from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_set:
                # Return [0, 1] rather than [0, 0] for case: [5, 5] ---> 10
                if diff != num:
                    j = nums.index(diff)
                else:
                    # Return [1, 2] rather than [1, 1] for case: [2, 5, 5, 11] ---> 10
                    try:
                        j = nums[i + 1 :].index(diff) + i + 1
                    except ValueError:
                        # continue, since another pair is guaranteed (by problem statement)
                        continue
                return [i, j]
        return [-1, -1]


sol = Solution()
cases = [
    ([3, 4, 5, 6], 7, [0, 1]),
    ([4, 5, 6], 10, [0, 2]),
    ([5, 5], 10, [0, 1]),
    ([2, 5, 5, 11], 10, [1, 2]),
    ([1, 3, 4, 2], 6, [2, 3]),
]

for nums, target, expected in cases:
    print(f"{nums} ---> {target}")
    actual = sol.twoSum(nums, target)
    print("assert {expected} == {actual}")
    print(f"assert {expected} == {actual}")
    print()
    assert expected == actual
