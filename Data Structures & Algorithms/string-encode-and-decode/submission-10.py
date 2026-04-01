class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sl =  []
        res = ""
        for s in strs:
            sl.append(len(s))
        for sz in sl:
            res += str(sz)
            res+= ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sl = []
        res = []
        i = 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i+=1
            sl.append(int(cur))
            i+=1
        i+=1
        for sz in sl:
            res.append(s[i:i+sz])
            i+=sz
        
        return res
