# n = 10
# prime_count = 0

# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         prime_count += 1

# print(prime_count)


def countPrimes(self, n: int) -> int:
        prime_count = 0
        for i in range(1,n+1):
            count = 0
            for j in range(1, i +1):
                if i % j == 0:
                    count += 1
                if count == 2:
                    # print(i)
                    prime_count +=1
       
        return prime_count
    
print(countPrimes(1,10))