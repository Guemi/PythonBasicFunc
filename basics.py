#To enter more than a value in one line
n, m = map(int,input().split())

#List comprenhension use
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
