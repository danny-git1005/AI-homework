# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 01:24:41 2020

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

train_in1 = array([[0.68, 0.83, 0.21, 0.125],
                  [0.73, 0.75, 0.18, 0.1875],
                  [0.73, 0.79, 0.14, 0.125],
                  [0.83, 0.71, 0.11, 0.1875]])

train_in2 = array([[0.77, 0.73, 0.19, 0.25],
                  [0.68, 0.5, 0.17, 0.125],
                  [0.82, 0.71, 0.11, 0.1875],
                  [0.75, 0.78, 0.13, 0.1875]])

#train_sol = array([[0.2, 0.4, 0.2, 0.8, 0.8, 0.4, 0.5, 0.5, 0.6, 0.8, 0.8, 0.5]]).T
train_sol = array([[0.8, 0.8, 0.5, 0.8, 0.2, 0.4, 0.2, 0.5]]).T


random.seed(1)
nn_weight1 = 2 * random.random((4, 1)) - 1

random.seed(2)
nn_weight2 = 2 * random.random((4, 1)) - 1

random.seed(3)
nn_weight3 = random.random()

for i in range(200000):
    #print("\ni= ", i, "nn_weight=")
    #print(nn_weight)
    #print("\ni= ", i, "nn_weight2=")
    #print(nn_weight2)
    
    train_out1 = 1 / (1 + exp(-(dot(train_in1, nn_weight1)-2)))
    train_out2 = 1 / (1 + exp(-(dot(train_in2, nn_weight2)-1)))
    
    input_of_3 = vstack((train_out1,train_out2))
    
    train_out3 = 1 / (1 + exp(-(input_of_3*nn_weight3-0.1)))
    
    
    nn_weight3 += sum(dot(input_of_3.T,(train_sol - train_out3) * train_out3 * (1 - train_out3)))
    rebuild = nn_weight3*( train_sol - train_out3 )*(train_out3 * (1 - train_out3))
    adj1 = rebuild[:4]
    adj2 = rebuild[-4:]
    nn_weight2 += dot(adj2.T , train_out2 * (1 - train_out2))
    nn_weight1 += dot(adj1.T , train_out1 * (1 - train_out1))
    

    #nn_weight += dot(train_in.T,(train_sol - train_out) *(1-(train_out**2)))
    
    MSE = (train_out3 - train_sol)**2
    print("the MSE = \n")
    print(sum(MSE)/8)

test_in1 = array([[0.75, 0.74, 0.17, 0.1875],
                [0.82, 0.73, 0.1, 0.4375],
                [0.68, 0.6, 0.17, 0.1875],
                [0.7, 0.4, 0.19, 0.25]])

test_in2 = array([[0.73, 0.73, 0.18, 0.1875],
                [0.72, 0.75, 0.19, 0.25],
                [0.77, 0.74, 0.17, 0.25],
                [0.77, 0.73, 0.17, 0.1875]])

test_sol =  array([[0.8, 0.8, 0.69, 0.65, 0.5, 0.4, 0.5, 0.6]]).T

end = time.process_time()

test_out1 = 1/(1+exp(-dot(test_in1,nn_weight1)))
test_out2 = 1/(1+exp(-dot(test_in2,nn_weight2)))
input_of_3_2 = vstack((test_out1,test_out2))
test_out3 = 1 / (1 + exp(-(input_of_3_2*nn_weight3)))

print('\nthe final prediction is \n',test_out3)
print('the MSE = ')
print(sum((test_out3-test_sol)**2)/8)

print ("執行時間 = %f (s)" %(end-start))
