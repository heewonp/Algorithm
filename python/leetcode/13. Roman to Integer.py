class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M":1000, "D": 500, "C": 100,"L":50, "X":10, "V": 5, "I":1}
        
        temp = 0
        for i in range(len(s)-1):
            num = dic[s[i]]
            next_num = dic[s[i+1]]
            if(num>=next_num):
                temp += num
            else:
                temp -= num
        
        temp += dic[s[len(s)-1]]
            
        return temp
            
        