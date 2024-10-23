grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_set = sorted(set(students))
first_average = sum(grades[0])/len(grades[0])
second_average = sum(grades[1])/len(grades[1])
third_average = sum(grades[2])/len(grades[2])
fourth_average = sum(grades[3])/len(grades[3])
fifth_average = sum(grades[4])/len(grades[4])
average_score = {students_set[0]: first_average,
                 students_set[1]: second_average,
                 students_set[2]: third_average,
                 students_set[3]: fourth_average,
                 students_set[4]: fifth_average}

print(average_score)