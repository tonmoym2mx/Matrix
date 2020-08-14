# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:19:52 2020

@author: Tonmoy
"""
import numpy as np

#1. Some practices questions:
print("1. Some practices questions")    
a = np.array([
     [1,0,2],
     [2,1,3],
     [1,-2,1]])
b = np.array([
     [2,1,-2],
     [3,0,1],
     [0,5,1]])

y1= (3*b) - (2*a)
ab = a.dot(b)
ba = b.dot(a)
y4 = ab.dot(ab)
print("\nHere , A=")
print(a)
print("\nB=")
print(b)
print("\nSolution of 3B-2A")
print(y1)
print("\nSolution of AB")
print(ab)
print("\nSolution of BA")
print(ba)
print("\nSolution of (AB)^2")
print(y4)


#1.2
print("\n\n1.2.") 
a = np.array([
    [2,1,3],
    [1,-2,2],
    [1,2,1]
    ])
print("here , A =")
print(a)
y1= a.dot(a).dot(a) - 2*(a.dot(a)) - 9*a
print("\nSolution of A^3-2A^2-9A")
print(y1)

#1.3
print("\n\n1.3.") 
a = np.array([
    [-2,2,-3],
    [2,1,-6],
    [-1,-2,0]])
print("here A = ")
print(a)
y1 = a.dot(a).dot(a) + a.dot(a) - (21*a)
print("\nSolution of A^3 + A^2 -21A")
print(y1)
