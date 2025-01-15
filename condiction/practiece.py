
# note  
print("#"*80)
print(" you can whrite the first letter fo time unite or the full name " .center(80,"#").title())
print("#"*80)
age = int(input(" \'whate\' your age :"))
#  get age in all time unite 
unit= input ("chouse time unite : month , week , days , houre , minut , seconde :").lower().strip()
month = age * 12 
week = month *4 
days = age * 365 
houre = days * 24 
minut = houre * 60
seconde = minut *60 
if unit == "month" or unit=='m' :
    print(f"your live {month:,} month ")
elif unit == "week" or unit=='w':
   print(f"your live {week:,} week ")
elif unit == "days" or unit=='d':
   print(f"your live {days:,} days ")
elif unit == "houre" or unit=='h':
   print(f"your live {houre:,} houre ")
elif unit == "minut" or unit=='mn':
   print(f"your live {minut:,} minut ")
elif unit == "seconde" or unit=='s':
   print(f"your live {seconde:,} seconde ")
else : 
   print ( " this unite note defindesd ")
  