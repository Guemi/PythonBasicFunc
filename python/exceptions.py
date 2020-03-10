n = int(input())


for i in range(n):
    
    #b = input()

    try:
        a,b = map(int,input().split())
        print (a/b)
    except BaseException as e:
        print ("Error code:", e)
"""
for i in range(n):
	a,b = input().split()
	#b = input()

	try:
	    print (int(a) //  int(b))
	except BaseException as e:
	    print ("Error code:", e)
	
	except ZeroDivisionError as e:
	    print ("Error code:", e)
	except ValueError as e:
	    print ("Error code:", e)
	    """