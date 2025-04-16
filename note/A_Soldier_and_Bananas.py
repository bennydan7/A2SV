def borrow_money(k, n, w):
    total_cost = k * w * (w + 1) // 2
    return max(0, total_cost - n)


k, n, w = map(int, input().split())
print(borrow_money(k, n, w))
