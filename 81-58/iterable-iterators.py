# -----------------------------------------
#-- iterabole vs iterator
# -----------------------------------------

#  Iterable 
# [1] object contains data that can be iteeated upon 
# [1] Exaples (String , list , set , tuple , dictionary)
# --------------------------------------------
# iterator
# [1] object used to iterate over interable using next() method return 1 elment at a time
# [2] you can generate iterator from iterable when usong iter() methdo
# [3] for loop already calls iter() method on the iterable behind the scene 
# [4] gives "stopiteration" if theres no next elment 
#----------------------------------------------


#  Iterable 

# mystrig = "elmehdi" 
# for letter in mystrig  : 
#     print(letter,end=" " )
# myslist = [10 ,5,38,7,8,5]
# for i in myslist  : 
#     print(i,end=" " )


#  iterators 

monnom = "elmehdi"
myiter = iter(monnom)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))