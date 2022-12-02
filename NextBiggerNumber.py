def next_bigger(n):
    n = list(str(n))
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            n[i], n[i-1] = n[i-1], n[i]
            return int(''.join(n))
    return -1
    
    
