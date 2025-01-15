# split rsplit 
# faire une liste 
#  [sep , position ]

var1="i love python and php"
print(var1.split())
var2="i-love-python-and-php"
print(var2.split("-",2))
# rsplit 
print(var1.rsplit(" ",2))
print(var2.rsplit("-",3))

# center ([number],[separation]) 
m="elmehdi"
print(m.center(11))  # espace
print(m.center(11,"#"))  #hach
print(m.center(15,"@")) # @

# count =>  chercher et calculer le mot combien de fois ella a dans string 
# counr ([index],[start],[end])
s="i love python and php because python and php  is  very easy "
print(s.count("php",))
print(s.count("python",6,40))

# swapcase  => inverse les lettre majuscule à miniscule et inverse vrai 
o="I lOve PythoN"
l="i loVE pHp"
print(o.swapcase())
print(l.swapcase())

#startswith ([index] [start] [end ]) => commence par 
#endwith ([index] [start] [end ]) => fin par 
mm="i love python"
print(mm.startswith("l"))
print(mm.endswith("n"))
print(mm.startswith("p",7))
print(mm.endswith("e",2,6))