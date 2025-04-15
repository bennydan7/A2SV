def numRescueBoats(people,limit):
    people.sort()
    i = 0
    j = len(people) -1
    results = []

    while i <= j:
        if people[i] + people[j] <= limit:
            results.append((people[i], people[j]))
            i += 1
        else:
            results.append((people[j]))
        j -= 1

    return results

print(numRescueBoats(people = [1,2], limit = 3))
print(numRescueBoats(people = [3,2,2,1], limit = 3))
print(numRescueBoats(people = [3,5,3,4], limit = 5))
    