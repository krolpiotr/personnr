#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("----------------- The PHOENIX Developer Studio -----------------")
"""
@date:    2018-10-30
@author:  Piotr Krol
@website: simon-phoenix.se
This program is getting your name, surname and personnummer (ÅÅMMDD-NNNC)
"""

def num(s):
    try:
        return int(s)
    except ValueError:
        return str(s)

name = input("Enter your name: ")
surname = input("Enter your surname: ")
personnummer = input("Enter your Swedish personnummer: ")
print("")

gender = personnummer[-1:]

print("Your name is " + name + " " + surname)
print("Your gender is: %s" % (num(gender) % 2 and 'male' or 'female'))
