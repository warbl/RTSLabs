# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:16:56 2021

@author: alexl
"""

#

def main():
    test_numbers = [1,2,5,8,11,2,4,6,19]
    
    value = int(input("Enter an integer: "))
    
    above_count = 0
    below_count = 0
    for number in test_numbers:
        if number > value:
            above_count+=1
        elif number < value:
            below_count+=1

    print(test_numbers)
    print("Numbers above value: " + str(above_count))
    print("Numbers below value: " + str(below_count))

if __name__ == "__main__":
    main()
