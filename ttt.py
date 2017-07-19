def single():
    N = int(input())# the number of couples
    # the list of couples
    C = []
    C_extend = C.extend
    for i in range(N):
        temp = input().split(" ")
        C_extend(temp)
    M = int(input())# the number of guests
    L = input().split(" ")# the list of guests
    t = list(set(C) & set(L))# the same ID in guests and couples
    # the count of singles in the guests
    count = 0
    for j in range(0, 2*N, 2):
        if C[j] in t and C[j + 1] in t:
            count += 2
            L.remove(C[j])
            L.remove(C[j+1])

    L_new = [int(i) for i in L]
    L_new.sort()
    Number = M - count
    print(Number)
    for m in L_new:
        if m == L_new[-1]:
            print(m)
        else:
            print(m,end=' ')
single()