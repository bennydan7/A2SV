if __name__ == '__main__':
    N = int(input())
    list = []

    for i in range(N):
        command = input().split()
        argument = command[0]
       
        if argument == "insert":
            position, value = int(command[1]), int(command[2])
            list.insert(position,value)
        elif argument == "print":
            print(list)
        elif argument == "remove":
            value = int(command[1])
            list.remove(value)
        elif argument == "append":
            value = int(command[1])
            list.append(value)
        elif argument == "sort":
            list.sort()
        elif argument == "pop":
            list.pop()
        elif argument == "reverse":
            list.reverse()
        

            




            
        



