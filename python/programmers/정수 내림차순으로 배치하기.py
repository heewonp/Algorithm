def solution(n):
    n_sort = sorted(list(str(int(n))),reverse = True)
    return int("".join(n_sort))