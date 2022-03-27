class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        arr_sort = self.sort(arr)
        target.sort()
        
        return target == arr_sort
        
    
    def sort(self,arr):
        if len(arr) <= 1 : return arr
        
        pivot = arr[0]
        left_sort = [data for data in arr[1:] if data <=pivot]
        right_sort = [data for data in arr[1:] if data > pivot]
        
        arr_sort = self.sort(left_sort) + [pivot] + self.sort(right_sort)
        
        return arr_sort