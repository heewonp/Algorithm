class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        ticket_sum =0
        for i in range(len(tickets)):
            if i <= k:
                ticket_sum += min(tickets[i],tickets[k])
                
            else:
                ticket_sum+= min(tickets[i],tickets[k]-1)
        return ticket_sum