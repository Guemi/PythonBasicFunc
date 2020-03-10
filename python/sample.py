#double a,b
print ("Function that return more than a value")

def FunctionSwap(a,b):#a = 0.0, b = 0.0):
	a = a+b
	b = a-b
	a = a-b
	return (a,b)

x = float(input("value for x: "))
y = float(input("value for y: "))
tupla1 = FunctionSwap(x,y)
print(tupla1)