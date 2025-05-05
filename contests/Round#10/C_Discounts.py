def min_cost_with_coupons(n, prices, m, coupons):
    prices.sort()  
    total_sum = sum(prices)
    results = []

    for q in coupons:
        min_cost = total_sum - prices[-q] 
        results.append(str(min_cost))

    print("\n".join(results))

n = int(input().strip())
prices = list(map(int, input().split()))
m = int(input().strip())
coupons = list(map(int, input().split()))

min_cost_with_coupons(n, prices, m, coupons)

