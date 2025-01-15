#------------------
#----set---------
# [1] set item are ecvlosed in curly braces
# [2] set item not oroder and not indexing 
# [3] slicing can be done 
# [4] set has noly immutable data types (numbres, stings,tuple) list and dic are not
# [5] set items is unique 
#------------------
# not oroder and not indexing 

myset={"elmehdi" ,"tabi", 18}
print(myset)
# print(myset[0]) not indexing


# slicing can be done 
mysetone={1,2,3,4,5,6}
# print(mysetone[0:3]) not slacing 

#  has noly immutable data types
# mysettwo={"elmehdi" ,100,100.5,True,[1,2,3]} unhashable type: 'list'
mysettwo={"elmehdi" ,100,100.5,True,(1,2,3)}
print(mysettwo)

# items is unique 
mysetfour={"elmehdi","one","elmehdi" ,2 , 1 ,2}
print(mysetfour)

