# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
#

# number = int(input("entre votre age "))
# print(number)


# try :  #  teste le code and test error 
#     number = int(input("entre votre age "))
#     print("je suis le message de test ")
# except  : # if il y a une error affiche le message suivant 
#     print("movais c'est pas un  nombre ")
# else : # if il y a une error 
#   number += 20 
#   print(number )
# finally : # afficher dans tout les case 
#    print("je suis le meiller jour ici ")


#  advanced exemle  : 

try  : 
#   print(10/0) 
#   print(x)
    print(int("hello"))
except ZeroDivisionError: 
  print("on pas deviser par 0 ")
except NameError : 
  print("n'exect pas cette nome ")
except : 
  print("bonne error")
except ValueError : 
   print("je conais pas cette error ")