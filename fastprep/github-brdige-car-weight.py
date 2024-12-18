class Solution:
    def bridgeCarWeight(self, U: int, weight: list[int]) -> int:
        # 2 cars -> pop the oldest car on the bridge -> let the next one in if it doesn't result in overload
        on_bridge: list[int] = []  # length of 2
        # 1 2
        #   :( ?
        # 3   ?
        # 2 3 ?
        # 4 5

        n_sent_back = 0
        # first, allow 1st & 2nd car on
        on_bridge.append(weight.pop(0))
        on_bridge.append(weight.pop(0))
        while weight:
            # let car near end off bridge
            if len(on_bridge) > 1:
                on_bridge.pop(0)
            # let the next car on WHO FITS
            if on_bridge[0] + weight[0] > U:
                weight.pop(0)
                n_sent_back += 1
            else:
                on_bridge.append(weight.pop(0))

        return n_sent_back


sol = Solution()

RES = sol.bridgeCarWeight(U=9, weight=[5, 3, 8, 1, 8, 7, 7, 6])
print(RES)
assert RES == 4
