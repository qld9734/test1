#! /usr/bin/python
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
    PRINT (F"#USage : python {sys.argv[0]}{fasta}")
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

## 19
'''
import sys, gzip

if len(sys.argv) != 2:
    print (f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]

with gzip.open(f,'rb') as handle:
    for line in handle :
        line = line.decode("utf-8")
        print(type(line.strip()))
        sys.exit()
'''
## 20
''' 
import sys, collections, gzip

if len(sys.argv) != 2:
    print (f"#usage: python {sys.argv[0]} [covid19.fasta.gz]")
    sys.exit()

f = sys.argv[1]
d = {}
with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8").strip()
        if line.startswith(">"):
            continue
        for s in line:
            if s in d :
                d[s] +=1
            else : 
                d[s] = 1
with open ("result.txt","w") as handle:
    handle.write(f"A : {d['A']}\n")
    handle.write(f"T : {d['T']}\n")
    handle.write(f"G : {d['G']}\n")
    handle.write(f"C : {d['C']}\n")

#print(collections.Counter(line))
'''
## 21
'''
seq1 = "ATGTTATAG"

for i in range(0,len(seq1),3):
    print (seq1[i]) # indexing
    print (seq1[i:i+3]) # slicing
print (seq1[::-1]) # upsidedown

def comp2(seq:str)->str:

    d_seq = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    comp = ''
    for i in seq:
        comp += d_seq[i]
    return comp

def comp1(seq: str)->str:
    comp = ''
    for s in seq : 
        if s == 'T':
            comp += 'A'
        elif s == 'A':
            comp += 'T'
        elif s == 'G':
            comp += 'C'
        elif s == 'C':
            comp += 'G'
    return comp

if __name__ == __main__:
    if len(sys.argv) != 2:
        print (f"#usage: python {sys.argv[0]} [covid19.fasta.gz]")
        sys.exit()
    
print(comp1(seq1))
print(comp2(seq1))
'''
## 21
'''
import sys
seq1 = sys.argv[1]

for i in range(len(seq1)):
    if seq1[i:i+2] == 'TT':
        print (i, i+2, seq1[i:i+2])
'''
#-----------list------------#
## 22 
'''
l = [3,1,1,2,0,0,2,3,3]
Min = l[0]
Max = l[0]
for i in range(len(l)):
    if Min > int(l[i]) : 
        Min = l[i]
for j in range(len(l)):
    if Max < int(l[j]):
        Max = l[j]

print (Min)
print (Max)
'''
## 23
'''
import collections
l = [3,1,1,2,0,0,2,3,3]
dic = {}

for i in l:
    if i in dic :
        dic[i] +=1
    else :
        dic[i] =1
print (dic)
print(collections.Counter(l))
'''
#---------------file read-------------

## 24
'''
import sys

def readtxt (File_name : str) -> str:
    ret = ""
    with open (f , 'r') as handle:
        for line in handle:
            if line.startswith('>'):
                continue
            ret += line.strip()
    return ret

if __name__ == "__main__" :
    if len(sys.argv) !==2 :
        print (f"#usage: python {sys.argv[0]} [covid19.fasta.gz]")
        sys.exit()
f = sys.argv[1]
'''
 
## 25
'''
import sys
def readtxt (File_name : str) -> list:
    ret = []
    with open (f , 'r') as handle:
       for line in handle:
            if line.startswith('#'):
                header = line.strip().split(',')
                continue
            splitted = line.strip().split(',')
            d = dict(zip(header,splitted))
            ret.append(d)
    return ret

if __name__ == "__main__" :
    if len(sys.argv) != 2:
        print (f"#usage: python {sys.argv[0]} [covid19.fasta.gz]")
        sys.exit()

f = sys.argv[1]
print(readtxt(f))

## 26

import sys,json
def to_json (l: list) -> None:
    with open ("read_sample.json", 'w') as handle:
       json.dump(l, handle, indent = 4)

if __name__ == "__main__" :
    if len(sys.argv) != 2:
        print (f"#usage: python {sys.argv[0]} [covid19.fasta.gz]")
        sys.exit()

f = sys.argv[1]
print(readtxt(f))
'''

## 27
''' 
import sys

f = sys.argv[1]
d = {}

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        line = line.strip()
        for s in line:
            if s in d :
                d[s] +=1
            else : 
                d[s] = 1
print (d)
'''
## 28__class to make fasta counter
'''
import sys
class FASTA : 
    
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def count_base(self):
        with open (self.file_name,'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] +=1
                    else : 
                        self.count[s] = 1
    def get_length(self):
        for k,v in self.count.items():
            self.length += v

    def __len__(self):
        self.get_length()
        return self.length
   
if __name__ == "__main__" :
    if len(sys.argv) != 2:
        print (f"#usage: python {sys.argv[0]} [fasta]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.count_base()
    t.get_length

    print(t.count)
    print(t.length)
    print(len(t))
'''
## 29 __ count read fastq
'''
import sys

f = sys.argv[1]
d = {}

with open(f, 'r') as handle:
    for line in handle:
        line = line.strip()
        for i in range(0,len(line),4):
            for cnt in line[i]:
                if cnt in d :
                    d[cnt] +=1
                else : 
                    d[cnt] = 1
print(d)
'''

## 30 ___ FASTQ class
import sys
class FASTQ:
    def __init__(self,file_name:str):
        self.file_name = file_name
        self.read_num = 0

    def count_read_num (self):
        cnt = 0
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1

if __name__ == "__main__" :
    if len(sys.argv) != 2:
        print (f"#usage: python {sys.argv[0]} [fasta]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_read_num()
    print(t.read_num)                














