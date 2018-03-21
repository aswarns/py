#!/usr/bin/env python
import sys
import os
os.system('clear')

FILE_NAME_REAL_PATH = os.path.realpath(sys.argv[0])
FILE_NAME = sys.argv[0]
print FILE_NAME_REAL_PATH
print FILE_NAME

''' Till here it's just comments & default Program that i use for all programs as a "Set of Default Stuff"'''

def main():
  INPUT = raw_input(" Pls enter Yes/Y to continue the program ... >>>  ")
  YES = {'yes','Yes','y','Y'}
  while True:
    try:    
      if INPUT in YES:
        print (" Welcome to program ")
        break

      else:
        OFF = input(" Press Q/q to exit from Program %s " % FILE_NAME)
        if OFF in {Q,q,Quit, quit}:
          sys.exit()
        else:
          print ("Please close this progeam by Ctrl + C & restart it")



if __name__ == ("__main__"):
  main()
