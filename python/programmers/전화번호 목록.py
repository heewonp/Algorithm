def solution(phone_book):
    
    # 풀이 1
    #  phone_book.sort()
    
    # for i in range(len(phone_book)-1):
    #     if phone_book[i+1].startswith(phone_book[i]):
    #         return False
        
    # 풀이 2 
    phone_set = set(phone_book)
    for phone_num in phone_book:
        temp=''
        for num in range(len(phone_num)-1):
            temp += phone_num[num]
            if temp in phone_set:
                return False
    return True