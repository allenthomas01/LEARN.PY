# -*- coding: utf-8 -*-
"""TASK 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VxSJZfyF0zf955iVrLtCIZ3nb6na-AqA

1.Write a program that uses input to prompt a user for their name and then welcomes them.
"""

#please provide your answer here below this line
x=input("Enter your name")
print("Welcome",x)

"""2.Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature."""

#please provide your answer here below this line
c=float(input("Enter a temperature in celsius scale "))
f=float((c*(9/5))+32)
print ("The corresponding fahrenheit value of ",c,"is",f)

"""3.Write a Python program to convert degree to radian."""

#please provide your answer here below this line
import math
x=float(input("Enter angle in degree"))
r=x*(math.pi/180)
print("Corresponding degree value of ",x,"in radians is ",r)