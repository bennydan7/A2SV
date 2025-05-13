class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for element in parts:
            if element == "..":
                if stack:
                    stack.pop()
            elif element and element != ".":
                stack.append(element)
        return "/" + ("/").join(stack)