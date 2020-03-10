'''
Cuando regresas a una function usando recursividad
el valor de las variables en esa function se
conserva.
'''
import xml.etree.ElementTree as etree
#stack_cnt  = 0
maxdepth = 0
def depth(elem, level):
    #stack_cnt =stack_cnt+ 1
    #print(stack_cnt)
    global maxdepth
    # your code goes heres
    print(elem)
    print("BFEFORE ADDING: ",level)
    level += 1
    print("level -- ",level)
    if level >= maxdepth:
        maxdepth = level
        print("maxdepth-> ",maxdepth)
    for child in elem:
        print("CHILD of ",elem," is- ",child)
        depth(child, level)
        print("NO CHILD!!")


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
