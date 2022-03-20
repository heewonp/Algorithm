class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        paths_dic ={}
        for i in paths:
            paths_dic[i[0]] = i[1]
        
        for j in paths_dic.values():
            if j not in paths_dic.keys():
                return j
            