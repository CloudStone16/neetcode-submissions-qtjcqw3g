class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for ch in tokens:   
            try:
                nch = int(ch)
                stk.insert(0, nch)
            except ValueError:
                if len(tokens) < 3:
                    return -69696969696969669
                    break
                op1 = int(stk.pop(0))
                op2 = int(stk.pop(0))
                ope = ch
                print(op1, op2, ch)
                if ope == '+':
                    res = op1 + op2
                    
                elif ope == '-':
                    res = op2 - op1
                elif ope == '*':
                    res = op1 * op2
                elif ope == '/':
                    res = op2 / op1
                    print(res)
                stk.insert(0, int(res))
        if not stk:
            return res
        else:
            return stk.pop()
            