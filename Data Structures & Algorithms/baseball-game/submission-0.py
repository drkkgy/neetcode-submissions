class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+" and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            elif op == "C" and stack:
                stack.pop(-1)
            elif op == "D" and len(stack) >= 1:
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        return sum(stack)

        