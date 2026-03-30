class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0 for k in range(len(temperatures))]
        count = 0
        for i, t in enumerate(temperatures):
            if i == 0:
                stk.insert(0, i)
            if stk:
                if t > temperatures[stk[0]]:
                    while stk and t > temperatures[stk[0]]:
                        ind = stk.pop(0)
                        res[ind] = count - ind
                        print(res, stk)

            stk.insert(0, i)
            count += 1

        return res


