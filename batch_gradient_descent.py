# -*- coding: utf-8 -*-
"""Batch_Gradient_Descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QHbjIIUm4yABhQJIWw9yKozGQcrNHnsm
"""

import numpy as np
import random
import pandas as pd

from google.colab import drive 
drive.mount('/content/gdrive')

f=pd.read_csv('gdrive/My Drive/Iris.csv')
Theta1=[]
Theta2=[]
converged=False
alpha=1.115
ep=0.0001
iter=0
m=f.shape[0]
x=f.shape[0]
y=f.shape[1]
minofTheta1=0

print(f.shape[0],f.shape[1])

t0=np.random.random(f.shape[1])
t1=np.random.random(f.shape[1])



for i in range(len(f)):

        x=f.loc[i].at['X-Axis']
        y=f.loc[i].at['Y-Axis']

        J = sum([(t0 + t1*x - y)**2 for i in range(m)])
        #print('Total Error,J(Theat)',J)



         # for each training sample, compute the gradient (d/d_theta j(theta))
        grad0 = 1.0/m * sum([(t0 + t1*x - y) for i in range(m)]) 
        grad1 = 1.0/m * sum([(t0 + t1*x - y)*x for i in range(m)])
        #print('(d/d_theta),j(theta)',grad0,grad1)

        # update the theta_temp
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1
    
        # update theta
        t0 = temp0
        t1 = temp1
      
        
      
          


        # mean squared error
        e = sum([(t0 + t1*x - y)**2 for i in range(m)])

t0,t1

