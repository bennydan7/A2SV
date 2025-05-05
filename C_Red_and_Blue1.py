def max_prefix_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum

def red_and_blue():
    t = int(input())  
    results = []
    
    for _ in range(t):
        n = int(input())  
        r = list(map(int, input().split())) 
        m = int(input())  
        b = list(map(int, input().split()))  
        
        max_red = max_prefix_sum(r)
        max_blue = max_prefix_sum(b)
        
        results.append(max_red + max_blue)
    
  
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    red_and_blue()