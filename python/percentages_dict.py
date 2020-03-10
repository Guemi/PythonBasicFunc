#dict = {'j':(1,2),'e':(2.4)} - Could be tuple or list
#print((dict))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        print("%.2f" %(sum(student_marks[query_name])/3))
    else:
        print("Name",query_name," is not listed!")
