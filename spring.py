# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    2 11 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

import math

K = int(input('spring constants: '))
F_t = int(input('total force: '))
c = str(input('enter configuration of series or parallel: '))

if c in ['Series, series']:
    x = F_t/K
    F1 = F_t
    F2 = F_t
    x1 = x/2
    x2 = x
    K1 = 1/(F1*x1)
    K2 = 1/(F2*x2)
    
    
if c in ['Parallel, parallel']:
    x = F_t/K
    x1 = x
    x2 = x
    F1 = F_t/2
    F2 = F_t
    K1 = F1*x1
    K2 = F2*x2
    