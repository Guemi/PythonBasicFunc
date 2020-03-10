if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)

    runner_up = min(arr)
    first = max(arr)
    #print("1--",first)
    for i in range(len(arr)):
    	if(arr[i]<first and arr[i]>=runner_up):
            runner_up = arr[i]
    	#print(arr[i])

    print(runner_up)
