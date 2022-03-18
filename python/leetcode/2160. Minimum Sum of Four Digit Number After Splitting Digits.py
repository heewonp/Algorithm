class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = list(map(int,str(num)))
        num_list = sorted(num_list)
        
        return int(num_list[0]*10)+int(num_list[1]*10)+int(num_list[2])+int(num_list[3])