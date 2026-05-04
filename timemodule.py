import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
T=int(time.strftime('%H'))
if (T<12):
 print("Good Morning")
elif (T>=12 and T<17):
  print("Good Evening")
elif (T>17 and T<24):
  print("Good night")    
  #https://docs.python.org/3/library/time.html time.strftime
