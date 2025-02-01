from typing import List


class Solution:

    i = 0  # Start at the first index (one's digit place)

    def plusOne(self, digits: List[int]) -> List[int]:

        def inc_next():
            """Recursive function."""

            # Sanity test
            if digits[self.i] > 10:
                raise ValueError(f"ERROR: {self.i}-index larger than 10: {digits}")

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Recursive step (if we have > 9 in the ith place)
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if digits[self.i] > 9:

                # Handle the case where the digits array needs an index added to the front
                if self.i == n - 1:
                    digits.append(1)
                    digits[self.i] = 0
                    return

                # Set to zero and increase next place
                digits[self.i] = 0
                self.i += 1
                digits[self.i] += 1

                inc_next()  # Recursive call

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Main logic
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        n = len(digits)
        digits.reverse()  # Reverse the digits for developer convenience
        digits[self.i] += 1  # Initial increment of one's place
        inc_next()  # Call to recursive function
        digits.reverse()  # Put back in original order

        return digits


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test cases
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sol = Solution()

cases = [
    # My test cases
    # (),
    # NeetCode test cases
    ([1, 2, 3, 5], [1, 2, 3, 4]),
    ([1, 0, 0, 0], [9, 9, 9]),
]

# Run tests
for expected, _input in cases:
    print(_input)
    actual = sol.plusOne(_input)
    print("assert {expected} == {actual}")
    print(f"assert {expected} == {actual}")
    print()
    assert expected == actual
