#!/usr/bin/env python3
''' per head calulcation  with tip percenatage calculations'''
import sys
import os
#file_name = os.path.basename(sys.argv[0])
#file_name = sys.argv[0]
file_name = os.path.realpath(sys.argv[0])
os.system('clear')
#print " enter Q/q anytime you wants to exit from Program "


def ashu():

  while True:
    NAME = input("Pls enter your name >> ")
    if NAME.isalpha():
      #if NAME == "q" or NAME == "Q":
        #sys.exit('\n \n  Your exiting from the :- %s \n \n \n ' % file_name)
      break
    else:    
      print (" Enter letters from A-Z or a-z ... >>")



  while True:
    try:
      AMOUNT = float(input(" Pls enter the bill amount ...>> "))
      break
    except:
      print (" \n Must be a number \n")



  while True:
    try:
      PEOPLE = float(input(" How many people... >> "))
      break
    except:
      print (" \n Must be a number \n")



  while True:
    try:
      TIP = float(input(" What\'s the pertenage of TIP...>> "))
      break
    except:
      print (" \n Must be a number \n")


  PER_HEAD = round(AMOUNT / PEOPLE, 2)
  TIP_PAY = round(PEOPLE / ( TIP / AMOUNT * 100), 2)
  TOTAL = round(PER_HEAD + TIP_PAY, 2)


  print ("each person would pay %s " % PER_HEAD)
  print ("each person pays tip ....%s" % TIP_PAY)

  print (" Hello %s, Which means every person should pay  ....%s Rs./-"  %(NAME, TOTAL))

if __name__ == ("__main__"):
  ashu()
