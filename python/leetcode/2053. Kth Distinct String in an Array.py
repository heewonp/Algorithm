class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        arr_dic ={}
        
        for i in arr:
            if i in arr_dic:
                arr_dic[i] += 1  
            else:
                arr_dic[i] =1
                
        cnt = 0
        for j in arr_dic:
            if arr_dic[j] == 1:
                cnt += 1         
                if cnt == k:
                    return j
        
        return ""