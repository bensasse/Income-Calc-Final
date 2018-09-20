#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:35:16 2018

@author: Summit
"""
import sys
sys.version

from collections import defaultdict as dd
import re



def income():
    income = dd(int)
    income_list=["check one","check two", "check three", "check four","misc income"]
    for c in income_list:
        income[c] = int(input("enter{}: ".format(pretty(c))))
    return income
c=income()
    
######Budget Side########

 
     
def costs():
    costs=dd(int)
    cost_list=["food cost","rent cost", "monthly payment1","monthly payment2", "car insurance", "gas","misc"]
    for z in cost_list:
        costs[z]=int(input("Enter {}: ".format(pretty(z))))
    return costs

def pretty(s):
    a=re.split("[A-Z]", s)
    return " ".join(a)
 
z=costs()
print (sum(c[i] for i in c - sum(z[i] for i in z)))

