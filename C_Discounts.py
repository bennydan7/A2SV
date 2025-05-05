# Input reading
n = int(input())                      
a = list(map(int, input().split()))  
m = int(input())                     
q = list(map(int, input().split())) 


a.sort(reverse=True)


total_sum = sum(a)


results = []
for coupon in q:
    free_bar = a[coupon - 1]
    cost = total_sum - free_bar
    results.append(cost)


for res in results:
    print(res)
