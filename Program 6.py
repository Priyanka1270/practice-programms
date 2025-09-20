#Write a program to print calendar

import calendar
year = int(input("Enter the year: "))
mm   = int(input("Enter the month: "))
cal  = calendar.month(year,mm)
print(cal)