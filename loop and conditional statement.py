# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:37:16 2023

@author: Sai khairnar
"""

#conditional statements
#if statement

a= 20
if a>20:
    print("a is big")
elif a<20:
    print("a is small")
else:
    print("a is medium")
    

name=input("enter your name:")
if (name=="tom"):
    print("welcome",name)
else:
    print("welcome guest")

#another example of if statement

std1=int(input("percentage obtained in exam:"))
if std1 in range(91,100):
    print("grade A")
elif std1 in range(81,90):
    print("grade B")
elif std1 in range(71,80):
    print("grade C")
elif std1 in range(50,70):
    print("grade D")
else:
    print("fail")
    

#looping statement using def
def count_to_10():
    for i in range(11):
        print(i)
count_to_10()

#example
def count_to_n(n):
    for i in range(1,n+1):
        print(i)
count_to_n(5)

#for loop
for x in range(10):
    print(x)

#nested loop
words =["carrot","cabbage","potato","brinjal"]
for word in words:
    print("indivisual words",word)
    for letter in word:
        print("indivisual letters",letter)

