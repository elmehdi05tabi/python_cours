# index ([substing] [start] [end]) => calculer et affiche le placement
#  de index 
a="i love python"
print(a.index("p")) #index) => 7
print(a.index("p",0 , 10)) #index) => 7
# print(a.index("p",0 , 5)) #index) =>error


#  find ([substing] [start] [end]) =>  calculer et affiche le placement
#  de index  si il y a une error effiche -1 et pas stope traitment 
b="i love python"
print(a.find("p")) #index) => 7
print(a.find("p",0 , 10)) #index) => 7
print(a.find("p",0 , 5)) #index) =>-1


# rjust([retourn] [index]) ,  ljust([retourn] [index]) 

c="elmehdi"
t=c.rjust(11)
print(c.rjust(11,"#"))
print(c.ljust(11,"#"))

# splitline => faire une list  chaque index=line 
d = """
elmedi
tabi
18 
ans 
"""
print(d.splitlines())
e= "signe \n le \n cheque "
print(e.splitlines())

f = "i\tlove\thtml\tand\tcss"
print(f.expandtabs(2))

### bollean 

dd="I Love Pythopn"
print(dd.istitle()) # true 
print(dd.islower()) # false 
print(dd.isupper()) # false 

bb=""
print(bb.isspace()) # true 

#isidentfier => donne si cette variables vrai pour l'uttilusation ou non
n="elme00dhi"
m="elmehdi00"
s="elmehdi--bb"
c="elmehdi_bb"
print(n.isidentifier()) # true  
print(m.isidentifier()) # true 
print(s.isidentifier()) # false 
print(c.isidentifier()) # true 

# isalpha  => donner c'est une alpha ou non
# isalnum  => donner c'est une alpha numérique ou non

aa="aaabbb"
bb="aaabbb11"
print(aa.isalpha()) # true 
print(bb.isalpha()) # false
print(bb.isalnum()) # true
print(bb.isalnum()) # true
