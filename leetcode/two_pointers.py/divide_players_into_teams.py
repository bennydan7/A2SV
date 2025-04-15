def divide_players(skill):
    n = len(skill)
    skill.sort()
    sum_skills = sum(skill)
    results = []

    left = 0
    right = n - 1
    
    valid = sum_skills % (n//2)
    total_skill = sum_skills // (n//2)
    while left < (n // 2):
        if valid == 0:
            if skill[left] + skill[right] != total_skill:
                return -1
            results.append((skill[left],skill[right]))
            left += 1
            right -= 1
        else:
            return -1
        
    output = sum(x * y for x,y in results)
    return output


    
print(divide_players(skill= [1,1,1,2,3,3,3,7,7,8,8,8,9,9]))
print(divide_players(skill=[2,1,5,2]))
print(divide_players(skill=[3,2,5,1,3,4]))
print(divide_players(skill=[3,4]))
print(divide_players(skill=[1,1,2,3]))