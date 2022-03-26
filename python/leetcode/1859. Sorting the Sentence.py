class Solution:
    def sortSentence(self, s: str) -> str:
        
        s_split = s.split()
        sort_s = sorted(s_split, key= lambda x: x[-1])
        
        res = ''
        for i in sort_s:
            res += i[:-1]+' '
            
        return res[:-1]
        