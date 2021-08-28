# problem : https://leetcode.com/problems/evaluate-reverse-polish-notation/
# solution :
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # loop over tokens
        for token in tokens:
            if token not in ops: # number
                stack.append(token) # push new number
            else : # operation
                tmp = int(ops[token](int(stack[-2]),int(stack[-1])))
                stack.pop()
                stack.pop()
                stack.append(tmp)
        return stack[0]
                
                
