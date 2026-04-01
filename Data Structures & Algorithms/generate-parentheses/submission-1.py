class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s='',o=0,c=0):
            if len(s) == 2*n:
                res.append(s)
            if o<n:
                backtrack(s+'(',o+1,c)
            if c<o:
                backtrack(s+')',o,c+1)
        backtrack()
        return res