def kid_with_candies(candies,extraCandies):
    n = len(candies)
    max_candies = max(candies)
    result = []
    for i in range(n):
        candies[i] += extraCandies
        if candies[i] >= max_candies:
            result.append(True)
        else:
            result.append(False)
    
    return result



print(kid_with_candies(candies = [2,3,5,1,3], extraCandies = 3))
print(kid_with_candies(candies = [4,2,1,1,2], extraCandies = 1))
print(kid_with_candies(candies = [12,1,12], extraCandies = 10))