if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_ = 0
    for i in range(len(student_marks[query_name])):
        sum_ += student_marks[query_name][i]
    
    # print(sum_/len(student_marks[query_name]))
    print(f"{sum_/len(student_marks[query_name]):.2f}")  # :.3f -> denotes print 3 decimal digits after the number!
