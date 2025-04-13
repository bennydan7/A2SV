def max_coins(piles):
    piles.sort(reverse = True)
    total = 0
    n = len(piles) // 3
    for i in range(1, n * 2,2):
        total += piles[i]
    return total


print(max_coins(piles = [2,4,1,2,7,8]))
print(max_coins(piles = [2,4,5]))
print(max_coins(piles = [9,8,7,6,5,1,2,3,4]))
