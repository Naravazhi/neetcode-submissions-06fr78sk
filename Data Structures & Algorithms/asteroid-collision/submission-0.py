class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # options
            # first is they both head in same direction
            # second is an asteroid going left meets an asteroid going right (i.e. negative after postiive)
            # 
            #
            # going left
            if asteroid < 0: 
                alive = True
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) < abs(asteroid):
                        stack.pop()
                        continue
                    elif abs(stack[-1]) > abs(asteroid):
                        alive = False
                        break
                    else:
                        alive = False
                        stack.pop()
                        break
                if alive:
                    stack.append(asteroid)

            else:
                stack.append(asteroid) 
        return stack