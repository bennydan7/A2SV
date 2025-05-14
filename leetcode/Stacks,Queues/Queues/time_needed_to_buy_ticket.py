def time_required_to_buy(tickets,k):
    time = 0

    while tickets[k] > 0:
        for i in range(len(tickets)):
            if tickets[k] == 0:
                return time
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1
    return time



print(time_required_to_buy( tickets = [2,3,2], k = 2))
print(time_required_to_buy(tickets = [5,1,1,1], k = 0))

