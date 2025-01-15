# nom="elmehdi"
# print("e"in nom) # true 
# print("m"in nom)  # true 
# print("s"in nom)  # false 
# print("b" not in nom)  # true 
# print("d" not in nom)  # false 
countrywin="morroco"
country= []
for i in range(5):
    a=input("entre you country:")
    country.append(a)
print(country)

if  countrywin in country :
    print("coungratolation you country is win in this compitition:") 
else:
    print("sorry your country is not win in this competion : ")
