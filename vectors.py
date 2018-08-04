# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 00:41:08 2018

@author: MOBASSIR
"""

"""
QUIZ : Suppose we represent n-vector by n-element lists. Write a procedure addn(v,w) to

compute the sum of two vectors so represented

"""

def addn(v, w): return [v[i] + w[i] for i in range(len(v))]


"""
QUIZ : Suppose we represent n-vectors by n-element lists.write a procedure 
scalar_vector_mult(alpha, v) that multiplies the vector v by the scalar alpha.
"""

def scalar_vector_mult(alpha, v): return [alpha*x for x in v]

w = [3,6,9,2,5,78]
v=[1,6,9,3,45,88]
alpha = 0.1

scalar = scalar_vector_mult(alpha, v)

add = addn(v, w)

print(scalar)
print(add)