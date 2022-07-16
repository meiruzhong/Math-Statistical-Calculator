# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:23:17 2022

@author: 1
"""
import numpy as np
import pandas as pd
import sys
import statistics 

#%%
#Mathematical mode building block
#define a is_valid function to check if values are valid
def is_valid(text):
    numbers = '0123456789.QC'
    for value in text:
        if numbers.find(value) == -1:
            return False
    return True

#define a is_valid_operator function to check if the operator is valid
def is_valid_operator(text):
    operators = '+-*/QC'
    for value in text:
        if operators.find(value) == -1:
            return False
    return True

#define addition function
def add(x,y):
    return x+y
#define subtraction function
def subtract(x,y):
    return x-y
#define multiplication function
def multiply(x,y):
    return x*y
#define division function
def divide(x,y):
    return x/y

#define mathematical_mode function, which can be used later
def math_mode():
    print('\nThis is mathematical mode. If you want to change mode to statistical one, please press C. If you want to quit, please press Q.')
    print('\nPlease enter the following items: ')
#input the first number and verify it
#if the number is C, the mode changes to the statistical mode.
#if the number is Q, it quits.
#if not above situations, it converts to float type
    num1 = input('The first number: ')
    while is_valid(num1) != True:
        print('please enter a valid figure with numbers only!')
        num1 = input('The first number: ')
    if num1 == 'C':
        if __name__ == '__main__':
            statistics_mode()
    elif num1 == 'Q':
        sys.exit()
    else:
        num1 = float(num1)
        
#choose operator and verify it
#if the operator is C, the mode changes to the statistical mode.
#if the operator is Q, it quits.
    print('\nThe operators include +, -, *, or / for addition, subtraction, multiplication or division, respectively.')
    operator = input('Enter an operator: ')
    while is_valid_operator(operator) != True:
        print('please enter a valid operator!')
        operator = input('The operator: ')
    if operator == 'C':
        if __name__ == '__main__':
            statistics_mode()
    elif operator == 'Q':
        sys.exit()
    else:
        #input the second number and verify it
        num2 = input('The second number: ')
        while is_valid(num2) != True:
            print('please enter a valid figure with numbers only!')
            num2 = input('The second number: ')
        if num2 == 'C':
            if __name__ == '__main__':
                statistics_mode()
        elif num2 == 'Q':
            sys.exit()
        elif num2 == '0':
            print('Error Occurred and Handled.')
            num2 = float(input('The second number: '))
        else:
            num2 = float(num2)
        
        #print the output of this calculation
        if operator == '+':
            output = add(num1,num2)
            print('\nOutput: ' + str(output))
        elif operator == '-':
            output = subtract(num1,num2)
            print('\nOutput: ' + str(output))
        elif operator == '*':
            output = multiply(num1,num2)
            print('\nOutput: ' + str(output))
        elif operator == '/':
            try:
                output = divide(num1,num2)
                print('\nOutput: ' + str(output))
            except(ZeroDivisionError):
                print('Error Occurred and Handled')

       #continue by usingthe previous output         
        while True:
            operator = input('Enter an operator: ')
            while is_valid_operator(operator) != True:
                print('please enter a valid operator!')
                operator = input('The operator: ')
            if operator == 'Q':
                break
            elif operator == 'C':
                if __name__ == '__main__':
                    statistics_mode()
            else:
                num = input('The next number: ') #input the next number
                while is_valid(num) != True:
                    print('please enter a valid figure with numbers only!')
                    num2 = input('The next number: ')
                if num == 'Q':
                    break
                elif num == 'C':
                    if __name__ == '__main__':
                        statistics_mode()
                else:
                    num = float(num) 
                    # get the new output
                    if operator == '+':
                        output = add(output,num)
                        print('\nOutput: ' + str(round(output,2)))
                    elif operator == '-':
                        output = subtract(output,num)
                        print('\nOutstatisticput: ' + str(round(output,2)))
                    elif operator == '*':
                        output = multiply(output,num)
                        print('\nOutput: ' + str(round(output,2)))
                    elif operator == '/':
                        try:
                            output = divide(output,num)
                            print('\nOutput: ' + str(round(output,2)))
                        except(ZeroDivisionError):
                            print('Error Occurred and Handled')

#%%
#Statistical mode building block
#define is_valid_stat() to validate the number inputted
def is_valid_stat(text):
    stats_mode = '0123456789.MSQC'
    for value in text:
        if stats_mode.find(value) == -1:
            return False
    return True

#define statistics_mode, which can be used later
def statistics_mode():
    print('\nThis is statistical mode. If you want to change mode to mathematical one, please press C. If you want to quit, please press Q.')
    values = [] #make a blank list
    value = 0 #blank variblae used in the loop
    i = 0 #index used in the values
    print('\nPlease enter the values you want to calculate Mean or Standard deviation!')
    print('Press either M for mean or S for standard deviation!')
    
    while True:
        value = input('Enter the value:')
        #if the user wants to calculate the mean
        if value == 'M':
            mean_v = np.mean(values)
            print('The total values are '+ str(values))
            print('The mean is '+ str(mean_v))
            sys.exit()
        #if the user wants to calculate the standard deviation
        elif value == 'S':
            std_v = np.std(values)
            print('The total values are '+ str(values))
            print('The standard deviation is '+ str(std_v))
            sys.exit()
        #if the user want to quit
        elif value == 'Q':
            sys.exit()
        #if the user want to change mode to mathematical one
        elif value == 'C':
            if __name__ == '__main__':
                math_mode()
        else: #insert the value to the lists
            value = float(value)
            values.insert(i,value)
            i += 1
            print(values)

#%%
#define a is_valid_mode function to check if the mode value is valid.
def is_valid_mode(text):
    numbers = '12'
    for value in text:
        if numbers.find(value) == -1:
            return False
    return True

#choose between Mathematical mode and Statistical mode
print('Please first choose between Mathematical mode and Statistical mode!')
mode = input('Clicking 1 for Mathematical mode or 2 for Statistical mode:')
#validate the mode value.
while is_valid_mode(mode) != True:
    print('please enter 1 or 2!')
    principal = input('Clicking 1 for Mathematical mode or 2 for Statistical mode:')

if mode == '1':
    math_mode()
elif mode == '2':
    statistics_mode()
        




