#on every year that is divisible by 4 with no remainder
#except every year that is evenly divisible by 100 with no remainder
#unless the year is also divisible by 400 with no remainder
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
