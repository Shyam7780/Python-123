def Time(time):
  hours=time//3600
  minutes=(time%3600)//60
  seconds=time%60
  return '{}H {}M {}S'.format(hours,minutes,seconds)
time=int(input("Enter time in seconds: "))
print(Time(time))