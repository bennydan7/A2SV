
# def find_the_runner_up(n: list):
#     n_s = set(n)
#     sorted_list = (sorted(n_s))
#     print(sorted_list)
#     runner_up = sorted_list[-2]
#     print(runner_up)

# find_the_runner_up([2,3,6,6,5])

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    def find_the_runner_up(arr):
        no_duplicate = set(arr)
        sorted_list = (sorted(no_duplicate))
        runner_up = sorted_list[-2]
        return runner_up
    
print(find_the_runner_up(arr))
    
    
    
    
    