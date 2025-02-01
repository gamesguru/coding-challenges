class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {s[0]: 0}
        t_dict = {t[0]: 0}
        # Load two dictionaries, tracking frequency of each char
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1

        # Check for equal length
        if len(s_dict) != len(t_dict):
            return False
        # Check for equal items and count value (maybe this can be simplified)
        for c in s_dict:
            if c not in t_dict:
                return False
            if s_dict[c] != t_dict[c]:
                return False
        for c in t_dict:
            if c not in s_dict:
                return False
            if t_dict[c] != s_dict[c]:
                return False
        return True


sol = Solution()
cases = [("racecar", "carrace"), ("jar", "jam")]

for s, t in cases:
    print(f"{s}, {t}")
    print(sol.isAnagram(s, t))
    print()
