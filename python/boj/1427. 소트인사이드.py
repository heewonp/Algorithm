n = input()

n_list = [int(i) for i in n]

sort_n = sorted(n_list, reverse=True)

for i in sort_n :
    print(i, end='')