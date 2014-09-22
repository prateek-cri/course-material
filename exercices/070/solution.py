# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:26:50 2014

@author: prateek
"""

a = 'abcdefghijklnmopqrstuvwxyz'
for i in a:
    for j in a:
        if i != j:
            print(i + j)
