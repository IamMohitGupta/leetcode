class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                l.append(int(tokens[i]))
            else:
                x = l.pop()
                y = l.pop()
                if tokens[i] == "+":
                    l.append(y+x)
                elif tokens[i] == "-":
                    l.append(y-x)
                elif tokens[i] == "*":
                    l.append(y*x)
                else:
                    l.append((int)(y/x))
        return l[0]
