from collections import deque
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack, total = deque(), 0
        
        for op in ops:
            if op == "C":
                total -= stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
                total += stack[-1]
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
                total += stack[-1]
            else:
                stack.append(int(op))
                total += stack[-1]
        
        return total
