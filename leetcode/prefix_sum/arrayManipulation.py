def arrayManipulation(n,queries):
    arr = [0] * (n + 1)
    
    for a,b,k in queries:
        arr[a] += k
        arr[b] -= k


