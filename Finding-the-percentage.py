#Finding the percentage

if __name__ == '__main__':

    #inputs n
    n = int(input())
    student_marks = {}
    #taking input of marks of students
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #taking the input of name of the student of which we need to find the percentage    
    query_name = input()

    #creating a list of marks of the required student
    marks = student_marks[query_name]

    #finding the percentage of the specified student
    average = sum(marks)/len(marks)
    print(f"{average:.2f}")
