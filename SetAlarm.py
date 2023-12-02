from datetime import datetime, timedelta
import time

def validateInput(tempHrs):
    if not tempHrs.isnumeric():
       tempHrs = input('Enter a number between 0 and 24 ')
       validateInput(tempHrs)
    elif tempHrs.isnumeric() and (int(tempHrs) > 24 or int(tempHrs)< 0):
       tempHrs = input('Enter a number between 0 and 24 ')
       validateInput(tempHrs)
    else:
       return int(tempHrs)

def validateWaitTime(tempWaitHrs):
   if not tempWaitHrs.isnumeric():
      tempWaitHrs = input('Enter a valid number for wait hours: ')
      validateWaitTime(tempWaitHrs)
   else:
      return int(tempWaitHrs)
   
currentHour = validateInput(input('Enter Timer Now - Current Hour: '))
waitTime = validateWaitTime(input('Enter wait time in hours: '))

today = datetime.now()
print("Today's date: {}".format(today))
timeTuple = (, , , currentHour, 00, 00, 00)
today = today.replace(*timeTuple)

time = today.time()
print("Only the time: {}".format(time))

print("Today's date: {}".format(today))
dt = datetime.strptime(str(today), '%Y-%m-%d %H:%M:%S.%f')
result = dt + timedelta(hours=waitTime)
print('{:%H:%M}'.format(result))

"""
currentDate = datetime.now()
print("Today's Date is ", end='')
print('{:%m/%d/%y}'.format(currentDate), end=' and time is ')
print('{:%H:%M}'.format(currentDate), end=' ')
dt = datetime.strptime(str(currentDate), '%Y-%m-%d %H:%M:%S.%f')
print()
result = dt + timedelta(hours=20)

print('{:%H:%M}'.format(result))
"""