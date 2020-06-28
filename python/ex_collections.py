from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print (Counter(myList))
money = 0
n_shoes = int(input())
shoe_sizes = map(int, input().split())
n_costumers = int(input())
cnt = Counter(shoe_sizes)

for i in range(n_costumers):
    size, price = map(int, input().split())
    # print(cnt[size])
    if(cnt[size] > 0):
        money = money + price
        cnt.subtract(Counter([size]))
        # print(cnt[size])
print(money)

        


        