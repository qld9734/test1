#!/bin/bash

echo "Hello"

for i in 1 2 3 4 5 
do
  #echo "sample_${i}"
  python 001.py ${i}
done
