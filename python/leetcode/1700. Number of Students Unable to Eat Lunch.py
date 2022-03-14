class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
 
# 풀이 1: 79ms       
#         temp = 0
#         while len(students) != temp:
#             if(students[0]==sandwiches[0]):
#                 temp =0
#                 students.pop(0)
#                 sandwiches.pop(0)
#             else:
#                 temp += 1
#                 pop_students =  students.pop(0)
#                 students.append(pop_students)
                
#         return len(students)

# 풀이 2 : 57ms
        students = deque(students)
        sandwiches = deque(sandwiches)
        temp = 0
        while len(students) != temp:
            if (students[0]==sandwiches[0]):
                temp =0
                students.popleft()
                sandwiches.popleft()
            else:
                temp +=1
                students.append(students.popleft())        
        return len(students)   