# -------------------------------------------------------
# -- Date and Time => introduction 
# -------------------------------------------------------
import datetime 
# print(dir(datetime))
# print(dir(datetime.datetime))

# print the current date and time
print(datetime.datetime.now())

print("="*50)
# print the current date and year
print(datetime.datetime.now().year)


# print the current date and month
print(datetime.datetime.now().month)


# print the current date and day
print(datetime.datetime.now().day)

print("="*50)

# print start and end of date 
print(datetime.datetime.min)
print(datetime.datetime.max)
print("="*50)

# print the current  time

# print(dir(datetime.datetime.now()))
print(datetime.datetime.now().time())
print("="*50)
# print the current  time hour
print(datetime.datetime.now().time().hour)
# print the current  time min
print(datetime.datetime.now().time().minute)
# print the current  time min
print(datetime.datetime.now().time().second)
print("="*50)
#  print the start and end time 
print(datetime.time.min)
print(datetime.time.max)
print("="*50)
# print specific date 
print(datetime.datetime(2005,5,25))
print(datetime.datetime(2005,5,25,10,45,20))
print("="*50) 

mybirthday = datetime.datetime(2005,1,12) 
datenow = datetime.datetime.now()
print(f"le temps actullemnt est : {mybirthday}",end=" ")
print(f"date now is {datenow}")

print(f"i lived for {(datenow - mybirthday).days} days ")

print(datetime.datetime.now().second) 