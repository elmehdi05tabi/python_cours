# -------------------------
# ----- Dictionary ------
# -------------------------

# [1] dic items are enclosed in curly braces 
# [2] dic items are contains key : value
# [3] dict key need to immutable => (number, string , tuple) list nite allowe
# [4] dict value can have any data type 
# [5] dic key need to be unique
# [6] dict not ordered you access its elmennt with key

# Dictionary

user ={
    "name":"elmehdi",
       "age":18,
       "contry":"morocco",
    #    [1,2,3,4]:"number"  unhashable type: 'list'
       "number":10.5,
       "viratai":True,
       "name":"tabi"
       }
print(user)
# ordered

# methde 1
print(user["contry"])

# methde 2
print(user.get('name'))

# print all keys in dect

print(user.keys())

# print all value in dect
print(user.values())

# two-dimension dictiobary 

langege ={
   "one" : {
       "name" :"html",
       "progresing" :" 80%"
   },
  "two": {
       "name" :"css",
       "progresing" :" 90%"
   },
   "three": {
       "name" :"js",
       "progresing" :" 100%"
   },
}
print(langege)
print(langege["one"])
print(langege.get('two'))
print(langege["three"]["name"])

#  dictionary lenght 
print(len(langege))
print(len(langege["three"]))

#  create dectinary from variales 

frworkone={
    "name" :"react js",
    "exrpercience":5.5
}
frworktwo={
    "name" :"bootsrap",
    "exrpercience":10
}
frworkthree={
    "name" :"anguler",
    "exrpercience":6
}
allfreemwok ={
"one":frworkone,
"two":frworktwo,
"three":frworkthree
}
print(allfreemwok)
print(allfreemwok["three"])



