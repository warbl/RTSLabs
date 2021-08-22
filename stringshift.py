# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:33:33 2021

@author: alexl
"""


#rotate string

def main():
    userString = input("Enter a string: ")
    userList = list(userString)
    
    rotations = int(input("Enter an integer to shift the string by: "))
    queue = []
 
    while(rotations > 0):
        queue.append(userList.pop())
        rotations -= 1
    
    while(queue):
        userList.insert(0, queue.pop(0))

    print("\nYour new string is: " + ''.join(userList))

if __name__ == "__main__":
    main()