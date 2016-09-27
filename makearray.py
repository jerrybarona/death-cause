# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:32:43 2016

@author: adars

"""
import sys
sys.path.append("numpy_path")

import numpy as np

def makearray(g,r,e,ye,pd,m,iw,race,ac,pi,icd,age):
    #y = np.zeros((13))
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    y[0] = int(r)
    y[1] = int(ye)
    y[2] = int(e)
    
    '''    
    if e == 0:
        y[1] = y
        y[2] = e
    elif e == 1:
        y[1] = 12
        y[2] = 1
    elif e ==2:
        y[1] = 16
        y[2] = 5
    elif e == 3:
        y[1] = 17
        y[2] = 6
    else:
        y[1] = 18
        y[2] = 8
    '''    

    y[3] = int(g)
    
    y[4] = 1
    
    y[5] = int(age)    
        
    if pd == 4:
        y[6] = 6
    else:
        y[6] = int(pd)
            
    y[7] = m
    
    y[8] = int(iw)
    
    if race == 4:
        y[9] = 0
    else:
        y[9] = int(race)+1
    
    y[10] == ac
    '''
    if ac == 1:
        y[10] = 8
    else:
        y[10] = 0
    '''
        
    if pi == 7:
        y[11] = 8
    else:
        y[11] = int(pi)
        
    y[12] = int(icd)
        
    '''
    if icd == 0:
        y[12] = 3735
    elif icd == 1:
        y[12] = 2075
    elif icd == 2:
        y[12] = 2173
    elif icd == 3:
        y[12] = 3442
    elif icd == 4:
        y[12] = 1037
    elif icd == 5:
        y[12] = 4871
    elif icd == 6:
        y[12] = 4
    '''
        
    return y
        
