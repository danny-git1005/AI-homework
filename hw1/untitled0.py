# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 01:52:26 2020

@author: user
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *
import time

start = time.process_time()

#train_in = array([[0.26, 0.73, 0.19, 0.25],
#                 [0.29, 0.73, 0.10, 0.4375],
#                 [0.29, 0.71, 0.11, 0.1875],
#                 [0.30, 0.71, 0.11, 0.1875],
#                 [0.21, 0.83, 0.21, 0.125],
#                 [0.23, 0.75, 0.19, 0.25],
#                 [0.24, 0.79, 0.14, 0.125],
#                 [0.25, 0.78, 0.13, 0.1875],
#                 [0.25, 0.73, 0.16, 0.125],
#                 [0,25, 0.74, 0.17, 0.1875],
#                 [0.24, 0.75, 0.18, 0.1875],
#                 [0.26, 0.74, 0.17, 0.25]])

train_in = array([[0.77, 0.73, 0.19, 0.25],
                  [0.73, 0.75, 0.18, 0.1875],
                  [0.82, 0.71, 0.11, 0.1875],
                  [0.83, 0.71, 0.11, 0.1875],
                  [0.68, 0.83, 0.21, 0.125],
                  [0.68, 0.5, 0.17, 0.125],
                  [0.73, 0.79, 0.14, 0.125],
                  [0.75, 0.78, 0.13, 0.1875],
                  [0.75, 0.73, 0.16, 0.125]
                  ])

#train_sol = array([[0.2, 0.4, 0.2, 0.8, 0.8, 0.4, 0.5, 0.5, 0.6, 0.8, 0.8, 0.5]]).T
train_sol = array([[0.2, 0.8, 0.2, 0.8, 0.8, 0.72, 0.5, 0.5, 0.6]]).T

random.seed(1)
nn_weight = 2 * random.random((4, 1)) - 1
for i in range(5000):
    #print("\ni= ", i, "nn_weight=")
    #print(nn_weight)

    train_out = 1 / (1 + exp(-dot(train_in, nn_weight)))
    print("train_out=")
    print(train_out)
    MSE = (train_out - train_sol)**2
    print("the MSE = \n")
    print(sum(MSE)/9)
 
    nn_weight += dot(train_out.T,(train_sol - train_out) * train_out * (1 - train_out))

test_in = array([[0.75, 0.74, 0.17, 0.1875],
                [0.82, 0.73, 0.1, 0.4375],
                [0.77, 0.74, 0.17, 0.25],
                [0.77, 0.73, 0.17, 0.1875],
                [0.73, 0.73, 0.18, 0.1875],
                [0.72, 0.75, 0.19, 0.25],
                [0.68, 0.6, 0.17, 0.1875],
                [0.7, 0.4, 0.19, 0.25],
                [0.72, 0.6, 0.17, 0.25]])

test_sol =  array([[0.8, 0.8, 0.5, 0.6, 0.5, 0.4, 0.69, 0.65, 0.7]]).T

end = time.process_time()
print('\nthe final prediction is ',1/(1+exp(-dot(test_in,nn_weight))))
print('the MSE = ')
print(sum((1/(1+exp(-dot(test_in,nn_weight))) - test_sol)**2)/9)
print ("執行時間 = %f (s)" %(end-start))
