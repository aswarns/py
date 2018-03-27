#!/usr/bin/env python3

import datetime

class MessageUser():
  user_details = []
  messages = []
  base_message = """ Hi {name}

  Thank you for the purchase on {date}.
  We hope to see you soon.
  Your total bill amount {total}.

  Team
  """

  def add_user(self,name,amount,email=None):
    name = name[0].upper() + name[1:].lower()
    amount = "%.2f" %(amount)
    detail = {
      "name": name,
      "amount": amount,
      }
    today = datetime.date.today()
    date_text = '{today.month}/{today.day}/{today.year}'\
                 .format(today=today)
    detail['date'] = date_text
    if email is not None: #if email != None
      detail["email"] = email
    self.user_details.append(detail)
  def get_details(self):
    return self.user_details
  def make_messages(self):
    if len(self.user_details) > 0:
      for detail in self.get_details():
        name = detail["name"]
        amount = detail["amount"]
        date = detail["date"]
        message = self.base_message
        new_msg = message.format(
                name = name,
                date = date,
                total= amount
                )
        self.messages.append(new_msg)
      return self.messages
    return[]


obj = MessageUser()
obj.add_user("Ashish", 232.3242, email='ashish.swarn.singh@oracle.com')
obj.add_user("Thakur", 22.32, email='ashish.swarn.singh@oracle.com')
obj.get_details()

print(obj.make_messages())


