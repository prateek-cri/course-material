# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 16:51:30 2014

@author: prateek
"""

import sys

sys.argv[1] = float(sys.argv[1])
sys.argv[3] = float(sys.argv[3])

op = sys.argv[2]
if op == '+':
    answer = sys.argv[1] + sys.argv[3]

elif op == '-':
    answer = sys.argv[1] + sys.argv[3]

elif op == '/':
    if sys.argv[3] == 0:
        print("Dividing by zero: Undefined Operation")
        exit()
    else:
        answer = sys.argv[1] / sys.argv[3]

elif op == '*':
    answer = sys.argv[1] * sys.argv[3]

elif op == '^':
    answer = sys.argv[1] ** sys.argv[3]

elif op == '%':
    answer = sys.argv[1] % sys.argv[3]

else:
    'Operation not recongnized; please use an operation from +-*/%^'
    exit()

print(answer)
