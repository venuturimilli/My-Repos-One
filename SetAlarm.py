#IMPORT REQUIRED LIBRARIES
from datetime import datetime, timedelta
import time

#FUNCTION TO VALIDATE CURRENT HOUR INPUT
def validateInput(tempHrs):
    if not tempHrs.isnumeric():
       tempHrs = input('Enter a number between 0 and 23: ')
       validateInput(tempHrs)
    elif tempHrs.isnumeric() and (int(tempHrs) > 23 or int(tempHrs)< 0):
       tempHrs = input('Enter a number between 0 and 23: ')
       validateInput(tempHrs)
    else:
       return int(tempHrs)
# FUNCTION TO VALIDATE WAIT TIME
def validateWaitTime(tempWaitHrs):
   if not tempWaitHrs.isnumeric():
      tempWaitHrs = input('Enter a valid number for wait hours: ')
      validateWaitTime(tempWaitHrs)
   else:
      return int(tempWaitHrs)

#GET CURRENT HOUR
currentHour = validateInput(input('Enter Timer Now - Current Hour: '))
#GET WAIT TIME
waitTime = validateWaitTime(input('Enter wait time in hours: '))
# GET TODAY'S DATE AND TIME
today = datetime.now()
#SET TIME TUPLE TO OVERRIDE THE CURRENT TIME TO USER GIVEN CURRENT TIME
timeTuple = (today.year, today.month, today.day, currentHour, 00, 00, 00)
today = today.replace(*timeTuple)
#GET TIME
time = today.time()
#PRINT DATE AND TIME THAT ALARM WAS SET 
print('The Alarm was set on the Date', end = ' ')
print(today.date(), end=' ')
print("and the time: {}".format(time), end =' ')
print('for', end =' ')
print( waitTime, end =' hours.\n')
#PRINT DATE AND TIME THAT ALARM IS GOING TO RING AT 
result = today + timedelta(hours=waitTime)
print('Alarm now rings at', end = ' ')
print('{:%H:%M}'.format(result), end = ' ')
print('on ', end= '')
print(result.date())
