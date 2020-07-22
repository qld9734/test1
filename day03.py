#! /usr/bin/python python

## 01 class_
'''
class C:

    def __init__(self):
        print ("Instance of class C made")
        self.name = "CCC"
        self.age = 0

    def say_hi(self):
        print("Hi")
    def add_age(self, n:int):
        self.age += n

    def __str__(self):
        return "__str__call"

    def __repr__(self):
        return "__repr__call"

    def __len__(self):
        print("__len__call")
    
    def __abs__(self):
        print("__abs__call")

    def __add__(self, other):
        return self.age + other.age
'''
## 02 __biopython
'''
from Bio import SeqIO

record = SeqIO.read("059.fasta", "fasta")

A = record.seq.count("A")
T = record.seq.count("T")
G = record.seq.count("G")
C = record.seq.count("C")

print(f"A: {A}") # 497 
print(f"T: {T}") # 514
print(f"G: {G}") # 585
print(f"C: {C}") # 444
'''
## 03 class FASTQ
'''
import sys

class FASTQ:

    def __init__(self, file_name:str):
        self.file_name = file_name
        self.read_num= 0
        self.base = {}

    def count_read_num(self):
        cnt1 = 0
        with open(self,file_name,'r') as handle:
            for line in handle:
                if cnt%4 == 0 :
                    header = line.strip()
                    self.read_num +=1
                elif cnt%4 == 1:
                    seq = line.strip()
                    for s in seq:
                        if s in self.base():
                            self.base[s] +=1
                        else :
                            self.base[s] = 1
                elif cnt%4 == 3:
                    qual = line.strip()
                cnt1 += 1

    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_base_num()

    print(t.read_num)
    print(t.base)
'''
## 04 _fibonacci_recursive programming
'''
n1= int(input("num: "))
def fib(n1:int) ->int:
    if n1 == 0:
        return 0
    elif n1 == 1:
        return 1
    elif n1 >=2:
        return fib(n1-1) + fib(n1-2)

print(fib(n1+1))
'''

## 05_k-mer

import sys

def kmer(base1,base2,n):
    if n == 1:
        return base1

    l_temp = []
    for i in base1:
        for j in base2:
            l_temp.append(i+j)

    return kmer(base1, l_temp, n-1)


base1 = ['A','C','T','G']
base2 = ['A','C','T','G']
n = int(sys.argv[1])
print(kmer(base1,base2,n))



    
