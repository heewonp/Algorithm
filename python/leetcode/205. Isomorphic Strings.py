class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_dict ={}
        t_set = set()
        
        for i in range(len(s)):
            if s[i] not in s_dict:
                if t[i] not in t_set:
                    s_dict[s[i]] = t[i]
                    t_set.add(t[i])            
                else:
                    return False
            else:
                if s_dict[s[i]] != t[i] :                   
                    return False
        return True