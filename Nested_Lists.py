if __name__ == '__main__':
    arr = []  
    scores_arr = []

    def nested_list(name, score):
        arr.append([name, score])
        scores_arr.append(score)

    for _ in range(int(input())):  
        name = input()
        score = float(input())
        nested_list(name, score)  


    sorted_scores = sorted(set(scores_arr))
    if len(sorted_scores) > 1:
        second_lowest_score = sorted_scores[1]

        second_lowest_students = []
        for name, score in arr:
            if score == second_lowest_score:
                second_lowest_students.append(name)

        second_lowest_students.sort()

        for student in second_lowest_students:
            print(student)
