class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    stack.append(op1 + op2)
                elif token == "-":
                    stack.append(op1 - op2)
                elif token == "*":
                    stack.append(op1 * op2)
                elif token == "/":
                    stack.append(int(op1 / op2))  # int() to truncate towards zero
        return stack[0]
