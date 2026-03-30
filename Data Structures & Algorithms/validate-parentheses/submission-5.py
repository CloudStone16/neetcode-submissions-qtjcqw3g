class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        flag = False
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stk.append(i)
                flag = False
            else:
                if not stk:
                    return False
                c = stk.pop()
                print(i, c)
                if (c == '(' and i == ')') or (c == '[' and i == ']') or (c == '{' and i == '}'):
                    print('true')
                    flag = True
                    continue
                else:
                    flag = False
                    return flag
                
        if stk:
            return False
        return flag
