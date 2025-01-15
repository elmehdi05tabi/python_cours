# ---------------
# -- Nested If --
# ---------------

uName = input("entre you name: ").strip()
isStudent = input("you are student: ?").strip()
uCountry =input("entre you country : ").strip()
cName = input(" what you cours you wanth: ? ").strip()
cPrice = 100

if uCountry == "morrocco" or uCountry == "KSA" or uCountry == "Qatar":

  if isStudent == "yes" :

    print(f"Hi {uName} Because U R From {uCountry} And Student")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

  else:

    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")


elif uCountry == "Kuwait" or uCountry == "Bahrain":

  print(f"Hi {uName} Because U R From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hi {uName} Because U R From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")