class Solution:
    def search(self, nums: list[int], target: int) -> int:
        mid = len(nums) // 2
        left = 0
        right = len(nums) - 1

        # check 3 points
        if nums[left] == target:
            return left
        if nums[mid] == target:
            return mid
        if nums[right] == target:
            return right

        while left < right:
            # Adjust left and right pointers
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
            # Return if we found it
            if nums[mid] == target:
                return mid
            # Adjust mid point
            mid = (left + right) // 2 + 1

        return -1


s = Solution()
tests = [
    ([-1, 0, 2, 4, 6, 8], 4, 3),
    ([-1, 0, 2, 4, 6, 8], 3, -1),
    ([5], 5, 0),
    ([2, 5], 2, 0),
]
for t in tests:
    _out = s.search(t[0], t[1])
    print(f"{t[0]}, target={t[1]}")
    print(f"Expected: {t[2]}    Actual: {_out}")
    print()
    assert _out == t[2]
