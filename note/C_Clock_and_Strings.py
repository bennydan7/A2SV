def is_intersect(a, b, c, d):
    a, b = sorted([a, b])
    c, d = sorted([c, d])
    
    in_arc = lambda x: a < x < b
    cond1 = in_arc(c) != in_arc(d)
    
    in_arc = lambda x: c < x < d
    cond2 = in_arc(a) != in_arc(b)
    
    return cond1 or cond2


t = int(input())
results = []
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if is_intersect(a, b, c, d):
        results.append("YES")
    else:
        results.append("NO")


print("\n".join(results))
