#!/usr/bin/env python
import datetime

default_names = ["ashish", "dd", "umesh", "venkat", "Santosh"]
default_amounts = [200,310,423,32324,312]

unf_message = """ Hi {name}!

    Thank you for the your help.
    Today's date is {date}, 
    total purchase is {total}
    
    Team
    {IDM}
    
    """
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
#print(text)

def make_messages(names,amounts):
  messages = []
  if len(names) == len(amounts):
    i = 0
    for name in names:
      new_msg = unf_message.format(
                name=name.title(),
                date=text,
                total=amounts[i],
                IDM='IDM PB Team'
                )
      i += 1
      print(new_msg)
      print("_"*30)


make_messages(default_names,default_amounts)


