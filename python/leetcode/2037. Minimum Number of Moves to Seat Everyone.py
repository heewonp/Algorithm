class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        cnt = 0
        for x,y in zip(sorted(seats),sorted(students)):
            cnt +=abs(x-y)
        
        return cnt
        