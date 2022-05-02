class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        g_dic = {}
        res = []
        for i,j in enumerate(groupSizes):
            if j not in g_dic or len(res[g_dic[j]]) == j:
                g_dic[j] = len(res)
                res.append([i])
            else:
                res[g_dic[j]].append(i)
        return res
                