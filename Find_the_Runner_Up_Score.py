
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    def find_the_runner_up(arr):
        no_duplicate = set(arr)
        sorted_list = (sorted(no_duplicate))
        runner_up = sorted_list[-2]
        return runner_up
    
print(find_the_runner_up(arr))
    
    
    
    
    