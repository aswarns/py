import time

def payments(bill,ppl):
  try:
    return round((bill/ppl),2)
  except:
    print("An error in payment calculations")


def tip(bill,perc,ppl):
  try:
    return round(((bill * (perc/100.00))/ppl),2)
  except:
    print("An error while calculation TIP")




def main():
  
  print(" How much is the Bill ? ")
  while True:
    try:
      total_bill = float(input(">> "))
      break
    except:
      print("\n You must enter a number value \n")


  print("How many people ?")
  while True:
    try:
      num_ppl = int(input(">>"))
      break
    except:
      print("\n Must be a number value \n")


  print("What Percentage of tip")
  while True:
    try:
      perc = int(input(">>"))
      break
    except:
      print("\n Must be a number Value \n")


  print("Calculating Plssss wait..>>")
  time.sleep(2)

  bill_payment = payments(total_bill, num_ppl)

  tip_payment = tip(total_bill, perc, num_ppl)

  total_payment = float(bill_payment) + float(tip_payment)

  print('\n\n\nEach person pays {} for the bill  '.format(str(bill_payment)))

  print('Each person pays {} for the tip'.format(str(tip_payment)))

  print('Each person pays total {}  '.format(str(total_payment)))


if __name__ == '__main__':
  main()
