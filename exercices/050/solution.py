# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:15:20 2014

@author: prateek
"""
sum = 0
for i in range(0, 1000):
    if (i % 3) == 0 or (i % 5) == 0:
        sum = sum + i
print(sum)
