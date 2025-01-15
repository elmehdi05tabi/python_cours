# --------------------------------------------
# -- Date and time => formate data 
# --------------------------------------------
import datetime 
mybirthday = datetime.datetime(2005,5,16)
print(mybirthday)
print(mybirthday.strftime("%a"))
print(mybirthday.strftime("%A"))
print(mybirthday.strftime("%b"))
print(mybirthday.strftime("%B"))
print(mybirthday.strftime("%d"))
print(mybirthday.strftime("%D")) 

print("="*40)
print(f"my birthday is =>{mybirthday.strftime("[%A-%B-%Y]")}")