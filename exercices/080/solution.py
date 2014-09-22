# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:30:35 2014

@author: prateek
"""
count = 0
a = 'abcdefghijklnmopqrstuvwxyz'
for i in a:
    count = count + 1
    for j in a[count:]:
        print(i + j)
