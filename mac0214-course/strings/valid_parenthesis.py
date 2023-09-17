# Problem: https://leetcode.com/problems/valid-parentheses/
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  38 ms / 16.32 MB /  a few seconds ago

class Stack(list):

    def top(self):
        return self[-1]
    
    def push(self, x):
        self.append(x)

    def empty(self):
        return self.__len__() == 0

class Solution:

    parenthesis_map = {
        "{": "}",
        "(": ")",
        "[": "]",
    }

    left = list(parenthesis_map.keys())
    right = list(parenthesis_map.values())

    def isValid(self, s: str) -> bool:

        if s[0] in self.right:
            return False

        stack = Stack([s[0]])

        i = 1
        while i < len(s):

            current = s[i]

            if current in self.right:
                
                try:
                    top = stack.top()
                except IndexError:
                    return False
                
                if self.parenthesis_map[top] != current:
                    return False
                
                stack.pop()

            else:
                stack.push(current)
            
            i += 1

        return stack.empty()
