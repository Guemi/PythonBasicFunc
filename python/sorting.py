toSort = list(input())
#digPart = [int(num) if(int(num)) else false for num in toSort]
#digPart = [if is_number(s): x = int(x) ]#else:]
digPart = []
alphaPart = []
for elem in toSort:
    try:
        #if(ele)
        digPart.append(int(elem))
    except Exception as e:
        #pass
        alphaPart.append(elem)

#odd = [oddNum for oddNum in digPart if(oddNum%2 != 0)]
odd = []
even = []
for num in digPart:
    if(num%2 == 0):
        even.append(num)
        #print(num)
    else:
        odd.append(num)
digPart = sorted(odd)+ sorted(even)#odd.sort() + even.sort()

upperLetters = []
lowerLetters = []
for letter in alphaPart:
    if(letter.isupper()):
        upperLetters.append(letter)
    else:
        lowerLetters.append(letter)
alphaPart = sorted (lowerLetters) + sorted(upperLetters)
sortedList = alphaPart + digPart
print(''.join(map(str, sortedList)))
'''
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
'''
