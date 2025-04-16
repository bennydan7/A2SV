def kid_with_candies(candies,extraCandies):
    n = len(candies)
    counter = 0
    max_counter = 0
    for i in range(n-1):
        candies[i] += extraCandies
        if candies[i] == 12:
            print("Yes")



