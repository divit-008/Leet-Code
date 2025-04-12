class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def generate(open_paren, close_paren):
            if open_paren == close_paren == n :
                result.append("".join(stack))
                return
            if open_paren<n :
                stack.append("(")
                generate(open_paren+1, close_paren)
                stack.pop()

            if close_paren<open_paren:
                stack.append(")")
                generate(open_paren, close_paren+1)
                stack.pop()        

        generate(0,0)
        return result