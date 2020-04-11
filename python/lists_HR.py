#!/usr/bin/env python

def insert_cmd(listX, i, e):
    listX.insert(i, e)

def print_cmd(listX):
    print(listX)

def remove_cmd(listX, e):
    listX.remove(e)

def append_cmd(listX, e):
    listX.append(e)

def sort_cmd(listX):
    listX.sort()

def pop_cmd(listX):
    listX.pop()

def reverse_cmd(listX):
    listX.reverse()

# def switch_cmd(cmd, listX, *arg):
#     cmd_list = {
#         'insert': insert_cmd(listX, *arg),
#         'print': print_cmd(listX),
#         'remove': remove_cmd(listX, *arg),
#         'append': append_cmd(listX, *arg),
#         'sort': sort_cmd(listX),
#         'pop': pop_cmd(listX),
#         'reverse': reverse_cmd(listX)
#     }
#     #cmd_list.get(cmd)
#     cmd_list.get(cmd, lambda: "Invalid Command")
    
if __name__ == '__main__':
    N = int(input())
    Mylist = [] #[x for x in range(12)]
    while(N>0):
        cmdStr = input().split()
        if(cmdStr[0] == 'insert'):
            insert_cmd(Mylist, int(cmdStr[1]), int(cmdStr[2] ) )
        elif(cmdStr[0] == 'print'):
            print_cmd(Mylist)
        elif(cmdStr[0] == 'remove'):
            remove_cmd(Mylist, int(cmdStr[1]))
        elif(cmdStr[0] == 'append'):
            append_cmd(Mylist, int(cmdStr[1]))
        elif(cmdStr[0] == 'sort'):
            sort_cmd(Mylist)
        elif(cmdStr[0] == 'pop'):
            pop_cmd(Mylist)
        elif(cmdStr[0] == 'reverse'):
            reverse_cmd(Mylist)
        #cmd_list.get(cmd)
        # cmd_list.get(cmdStr[0], lambda: "Invalid Command")
        
        # switch_cmd( cmdStr[0], Mylist, *[ *map( int,cmdStr[1:] ) ] ) 
        #print(Mylist)
        N -= 1
    

