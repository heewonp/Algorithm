class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        temp = []
        
        for i in bank:
            device = 0
            for j in i:
                if j == '1':
                    device += 1
            
            if device != 0:
                temp.append(device)
        
        res = 0
        for i in range(len(temp)-1):
            res += temp[i] * temp[i+1]
            
        return res