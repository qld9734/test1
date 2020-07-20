## 01
#print ("Hello Bioinformatics")

## 02
'''
import math
r=input('radius: ') # raius setting
area=int(r)**2*math.pi # area
print (round(area,2)) 
'''
## 03
'''
num1 =3
num2 =5
print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1*num2)
print(num1%num2)
print(num1**num2)
'''

## 04 
'''
num = int(input("num : "))
if num %2 == 0:
    print ("it\'s even")
else : 
    print ("it\'s odd")
'''

## 05
'''
num1 = 21
if num1%3==0 and num1%7==0:
    print('3x,7x')
elif num1%3 == 0:
    print('3x')
elif num1%7 == 0:
    print('7x')
else :
    print('none')
'''

## 06
'''
total = 0
for i in range(1,11):
    total += i
print (total)
'''

## 07
'''
for i in range(2,10,2):
    print()
    for k in range(1,10):
        print (i,"x",k,"=",i*k)
        print (f"{i} x {j} = {i*j}")
'''

## 08
'''
cnt = 1
a = 1
while cnt < 6 :
        a *= cnt
        cnt += 1 
print (a)
'''

## 09
'''
def greet() -> None :
    print ('Hello Bioinformatics')

greet()
'''

## 10
'''
def mySum(n1 : int, n2 : int) -> None :
    print (f"{n1} + {n2} = {n1+n2}")

mySum(2,3)
mySum(5,7)
mySum(10,15)
'''

## 10_2
'''
def mySum(n1 : int, n2 : int) -> int :
    #print (f"{n1} + {n2} = {n1+n2}")
    return n1+n2
'''
## 11
'''
name = input("name : ")
print (f"Hello {name}")
print (type(name))
'''
## 12
'''
name = input("name : ")
if name.isalpha :
    print(f"{name} is str") 
elif name.isnumeric :
    print(f"{name} is number")
else :
    print ("???")
'''

## 13
'''
import sys

print (f'run -> sample_{sys.argv[1]}')
'''

## 14
'''
import sys
f = sys.argv[1]

with open(f,"r") as handle :
    for line in handle :
        if line.startswith(">"):
            continue
        print(line.strip())
'''

## 15
'''
import sys, collections

if len(sys.argv) !=2:
    print (f"#usage : python {sys.argv[0]}{fasta}")
    sys.exit()

f = sys.argv[1]
d = {}

with open(f, "r") as handle :
    for line in handle :
        if line.startswith(">"):
            continue

        for s in line.strip() : 
            if s in d :
                d[s] += 1
            else :
                d[s] = 1

print (d)    
total = 0
for k,v in d.items():
    total += v
print (total)

#print(collections.Counter(line.strip()))
'''
## 16 
'''
f = "covid19.fasta"
with open(f, "w") as handle:
    handle.write(f"A : {d['A']}\n")
    handle.write(f"T : {d['T']}\n")
    handle.write(f"G : {d['G']}\n")
    handle.write(f"C : {d['C']}\n")
'''
## 17
'''
import sys

if len(sys.argv) != 2:
    print (f"#usage: python {sys.argv[0]}[txt]")
    sys.exit()

f = sys.argv[1]
try: 
    with open(f, 'r') as handle:
        read = handle.readlines()
    print(read)

except FileNotFoundError : 
    print(f"{f} not found.. please check")
    sys.exit()

print(read)
'''

## 18 
'''
import sys

if len(sys.argv) != 2:
    print (f"#usage: python {sys.argv[0]}[txt]")
    sys.exit()


try:
    num = int(sys.argv[1])
    print(10 / num)
except ZeroDivisionError:
    print ("that\'s nono")
    sys.exit()
except ValueError:
    print ("value error")
    sys.exit()
'''
