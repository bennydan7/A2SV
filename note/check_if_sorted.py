def arraySortedOrNot(arr) -> bool:
        # code here
        
        
        for i in range(len(arr)):
            if arr[i] > arr[i + 1]:
                return True
            else:
                return False
    
print(arraySortedOrNot(arr = [10, 20, 30, 40, 50]))
print(arraySortedOrNot(arr = [90, 80, 100, 70, 40, 30]))