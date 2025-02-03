class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Adjust string (according to problem statement)
        s = s.lower()  # Set to lowercase

        for c in set(x for x in s):
            if not c.isalnum():
                s = s.replace(c, "")  # Remove non-alphanumeric characters

        # Print adjusted string
        print(s)

        # Return false if a pair of approaching endpoint char pairs doesn't match
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test cases
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sol = Solution()

cases = [
    # My test cases
    (True, "a"),
    (False, "abcdba"),
    (False, "ab"),
    (True, "aa"),
    (True, "aaa"),
    (True, "aaaa"),
    (False, "aaba"),
    (False, "aaab"),
    # NeetCode test cases
    (True, "Was it a car or a cat I saw?"),
    (False, "tab a cat"),
    (True, "Madam, in Eden, I'm Adam"),
]

# Run tests
for expected, string in cases:
    print(string)
    actual = sol.isPalindrome(string)
    print("assert {expected} == {actual}")
    print(f"assert {expected} == {actual}")
    print()
    assert expected == actual
