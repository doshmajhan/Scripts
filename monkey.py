
def jump(A, D):
    if D > len(A):
        return 0
    lst = [0] * len(A)
    t = 0
    cur = 0
    sub = 0
    for i in range(0, len(A)):
        lst[A[i]] = i

    for i in range(0, len(A)):
        if lst[i] == -1:
            sub += 1
            continue

        if lst[i] > t:
            t = lst[i]
        
        if lst[i] > cur and D+cur >= lst[i]:
            cur = lst[i]
        
        if D + cur >= t:
            cur = t
            if cur + D >= len(A):
                return i - sub
        
    return -1

r = jump([1, -1, 0, 2, 3, 5], 3)
print r
r = jump([3, 0, 5, -1, 2, 1], 3)
print r
r = jump([3, 0, 5, -1, 2, 1], 2)
print r
r = jump([-1, 0, 1, 2], 2)
print r
