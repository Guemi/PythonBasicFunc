"""
Rangonli 

import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))

"""

import string
letters = list(string.ascii_lowercase)
#print(letters)

def print_rangoli(size):
    # your code goes here
    lenT = ((size-1 )*4 )+1 
    valStr = []
    for i in range(size): 
        strMid = [let for let in letters[(size-1-i):(size)]]
        strMid = strMid[::-1] + strMid[1:]
        strx = '-'.join(strMid)
        valStr.append(strx)
        str2print = '{:-^{}s}'.format(strx,lenT)
        print(str2print)
            
    for i in range(len(valStr)-1):
        strx = valStr[len(valStr)-2-i]
        str2print = '{:-^{}s}'.format(strx,lenT)
        print(str2print)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
