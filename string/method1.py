m = "bonjour mes chaires amis"
# len() => calculer le nombre des lettre en le chaine de caracére 

print(len(m))

# strip() , rstrip() , lstrip()
a="  comment t'as pas ta journée   "
# strip( suprime les espaces à gauche et droit )
print(a.strip())
# rstip (suprimé les espace droit c'est tout)
print(a.rstrip())
# lstrip(suprime les espace gouch c'est tout )
print(a.lstrip())

n="###hello world###"
print(n.strip("#"))
print(n.rstrip("#"))
print(n.lstrip("#"))


# title ( tout les premier letter majuscille )
#capitalize => la premier lettre dans le chaine majuscile c'est tout 
# upper => uppercase => text majuscule 
# lower => lowercase => text muniscule 
var="messi il a 8ballon d'or Mais cr7 il a5 "
print(var.title())
print(var.capitalize())
print(var.upper())
print(var.lower())

#zfill => faire zero aven le chaine 
a,b,c,d = "1","11","111","1111"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))