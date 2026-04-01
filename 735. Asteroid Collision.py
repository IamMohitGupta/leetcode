class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[asteroids[0]]
        for i in range(1,len(asteroids)):
            curr = asteroids[i]
            while stack and stack[-1] > 0 and curr < 0:
                if abs(stack[-1]) > abs(curr):
                    curr = 0
                    break
                elif abs(stack[-1]) == abs(curr):
                    stack.pop()
                    curr = 0
                    break
                else:
                    stack.pop()
            else:
                stack.append(curr)
        return stack
