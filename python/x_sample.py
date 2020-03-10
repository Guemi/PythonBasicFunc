# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
a = []
for n_tc in range(int(input())*2):
    _ = input()
    a.append(input().split())

x=0
while (x<n_tc):
    set1 = set(a[x])
    set2 = set(a[x+1])
    if (len(set1 & set2) >= len(set1)):
        print("True")
        #print(set1 & set2)
    else:
        print("False")#No common elements")
    x = x+2


a = []
for x in range(int(input())):
    a.append(x+1)

print(a)

for i in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))

for _ in range(int(input())):
x, a, z, b = input(), set(input().split()), input(), set(input().split())
print(a.issubset(b))

superset = set(input().split())
#a = "False"
for i in range(int(input())):
    temp = set(input().split())
    if(superset.issuperset(temp)):
        a = "True"
        #print(a)
    else:
        a = "False"
        break
        #print(a)

print(a)

def split_and_join(line):
    # write your code here
    line = "-".join(line.split(" "))
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

def print_full_name(a, b):
    print("Hello "+ a + " " + b + "!" + " You just delved into python")#.join(a).join(" "))
    print ("Hello {0} {1}! You just delved into python.".format(input(), input()))

if __name__ == '__main__':
    first_name,last_name = input(), input()
    print_full_name(first_name, last_name)

return(string[:position] + character + string[position+1:])

def count_substring(string, sub_string):
    count = 0
    #subStr_val = ord(sub_string)
    for i in range(len(string) - len(sub_string)):
        #temp = ''.join(string[i:i+(len(sub_string))])
        #print (temp)
        if(sub_string == string[i:i+(len(sub_string))]):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

def ret2val(a,b):
    a = a+b
    b = a-b
    return(a-b,b);
l,k = ret2val(5,10)
print(l,k)

def swap_case(s):
    #sw = lambda l : l if(not(l.isalpha())) else (l.upper() if (l.islower()) else l.lower())
    #return (''.join(list(map(sw,s))))
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

import textwrap

s = input()
wrapper = textwrap.TextWrapper(width=50)
st_w = wrapper.fill(text=s)
print(st_w)
print ("\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)]))

g = '-'
p = '.'
b = '|'
w = "WELCOME"
n,m = input().split()
n = int(n)
m = int(m)

for i in range((n-1)//2):
    #print(((m-1)//2)-i*3)
    #print(i)
    print(p.rjust((((m-1)//2)-i*3),g) + (b.ljust(3,p)*i) + b + (b.rjust(3,p)*i) + p.ljust((((m-1)//2)-i*3),g))

print(w.center(m,g))

for i in range(((n-1)//2)-1,-1,-1):
    #print(i)
    print(p.rjust((((m-1)//2)-i*3),g) + (b.ljust(3,p)*i) + b + (b.rjust(3,p)*i) + p.ljust((((m-1)//2)-i*3),g))

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

''''


#
