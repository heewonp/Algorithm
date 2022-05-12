class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        s_dic = {'R':[0,1],'L':[0,-1],'U':[-1,0],'D':[1,0]}
        res = [0] * len(s)
        
        for i in range(len(s)):
            x,y = startPos
    
            for j in range(i,len(s)):
                x += s_dic[s[j]][0]
                y += s_dic[s[j]][1]
                
                if 0 <= x < n and 0 <= y < n:
                    res[i] += 1
                else:
                    break       
        return res