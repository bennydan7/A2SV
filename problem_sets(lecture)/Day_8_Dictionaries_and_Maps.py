n = int(input())  
data = {}  

for _ in range(n):
    entry = input().split()  
    key = entry[0]  
    value = " ".join(entry[1:]) 
    data[key] = value 
    
    if key in data and value in data.values():
        print(f"{key} == {value}")
    else:
        print("Not found")


