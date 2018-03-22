import time

def main():


  while True:
    try:
      print('Whats the bill amount')
      bill = float(input(">> Rs.."))
      break
    except:
      print("\n Pls enter number value only\n")


  while True:
    try:
      print('Whats the number of people')
      people = int(input(">> people.."))
      break
    except:
      print("Pls enter number value only")


  while True:
    try:
      print('Whats the tip percentage')
      perc = float(input(">> %.."))
      break
    except:
      print("Enter number value")


  print("Calculation in progress..hold on\n \n ")
  time.sleep(2)

  bill_payment = round(float(bill/people),2)
  tip_payment = round(float(bill * (perc/100)),2)
  bill_tip  = round(float(bill + tip_payment),2)
  per_head = round(float(bill_tip / people),2)


  print("Each person pay without tip {}".format(bill_payment))
  print("Total Tip pay {}".format(tip_payment))
  print("Grand Total {}".format(bill_tip))
  print("\n\nFinal payment needs to be pay by per head... {}".format(per_head))



if __name__ == '__main__':
  main()
