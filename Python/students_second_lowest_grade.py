if __name__ == '__main__':
    students = []   
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])

    students.sort(key=lambda x: x[1])
    second_lowest = [x for x in students if x[1] != students[0][1]][0][1]
    second_lowest_students = [x[0] for x in students if x[1] == second_lowest]
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)

