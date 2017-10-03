# -*- coding: utf-8 -*-
"""
@title: Find PI to the Nth Digit
@function: Find PI to the Nth Digit - Enter a number and have the
 program generate PI up to that many decimal places.
@author: Zhilin
"""
import math
from decimal import *

def fac(n):
    '''
    compute the factorial of n
    '''
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return(ans)

def getdecimal(k):
    '''
    use Srinivasa Ramanujan's formula to compute Pi
    '''
    getcontext().prec=k+1
    ans=0
    for i in range(k+1):
        a=fac(4*i)*(1103+26390*i)
        b=(fac(i)**4)*(396**(4*i))
        ans += a/b
    out= Decimal(9801)/Decimal(ans*2*math.sqrt(2))
    return(out)

def main():
    '''
    the main function to complete the function
    Input number cannot more than 10000 and give warnings if
    the input character is invalid
    '''
    while True:
        try:
            num= int(input('Please input a number of decimals you want to get:'))
        except ValueError:
            print('Please input a valid number!')
            continue
        
        if num>10000:
            print('The number is too large, please input a number<10000!')
            continue
        
        print(getdecimal(num))
main()



