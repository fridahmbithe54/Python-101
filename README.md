# Fibonacci sequence checker
This repository contains a python file which is used to if a random input number belongs to a fibonacci sequence and returns a true or false
# for example
N = int(input("Enter the number of terms : "))
 
# first two terms are f1, f2 equal to 0 and 1 respectively
f1, f2 = 0, 1
count = 0
 
# checking for invalid inputs
if(N <= 0):
    print("Invalid Input, Kindly enter number greater than 0")
 
# if only one number in the sequence
elif(N == 1):
    print("Generating Fibonacci Sequence upto ", N, ": ")
    print(f1)
 
# for all the other cases, i.e. when N > 1
else:
    print("Generating Fibonacci sequence upto ", N, ": ")
    while count < N:
        print(f1)
        fth = f1 + f2

