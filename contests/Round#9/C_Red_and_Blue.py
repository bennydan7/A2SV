def max_prefix_sum(arr):
    current_sum = 0
    prefix_arr = [0] * len(arr)
    for i in range(len(arr)):
        current_sum += arr[i]
        prefix_arr.append(current_sum)
    return max(prefix_arr)

def red_and_blue():
    t = int(input())
    res = []

    for _ in range(t):
        n = int(input())
        r = list(map(int,input().split()))
        m = int(input())
        b = list(map(int,input().split()))

        max_red = max_prefix_sum(r)
        max_blue = max_prefix_sum(b)

        res.append(max_red + max_blue)

    print("\n".join(map(str,res)))
    
if __name__ == "__main__":
    red_and_blue()

    