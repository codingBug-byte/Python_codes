if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    values = []
    values .append(student_marks.get(query_name))
    avg = 0
    for i in values[0]:
        avg+=i
    print("{:.2f}".format(avg/3))

