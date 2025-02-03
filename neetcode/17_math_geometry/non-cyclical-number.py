class Solution:
    def isHappy(self, n: int) -> bool:
        # Track numbers we have seen already
        n_set = set()

        # Initialize local var
        num = n

        # Check for cycles
        while True:
            # Return trivial case
            if num == 1:
                return True

            # Add to list, and replace n
            n_set.add(num)
            num = sum(int(x) ** 2 for x in str(num))

            # Check if number was already visited
            if num in n_set:
                return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test cases
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sol = Solution()

cases = [
    # My test cases
    # (),
    # NeetCode test cases
    (True, 100),
    (False, 101),
]

# Run tests
for expected, _input in cases:
    print(_input)
    actual = sol.isHappy(_input)
    print("assert {expected} == {actual}")
    print(f"assert {expected} == {actual}")
    print()
    assert expected == actual
