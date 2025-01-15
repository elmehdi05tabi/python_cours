#-------------------------------
# --List--
#-------------------
# [1] list items ils a dans une square brackets 
# [2] list are ordered , to use index to access itams
# [3] list are mutables => add, delete, edit
# [4] list items is not unique 
# [5] list can have deffernet type 
#------------------------------- 
mylist=["one" , "two" , "one" , 1 , 10.5 , True ]
print(mylist) # tout list
print(mylist[1])#two
print(mylist[-1])# True
print(mylist[2:5])# ["one" , 1 , 10.5]
print(mylist[:4]) # ['one', 'two', 'one', 1]
print(mylist[2:]) #["one" , 1 , 10.5 , True]
print(mylist[::2]) # ["one",one ,10.5 ]

# -------------------------- MODIFIER----------------------
mylist2=["elmehdi",18,"morocco","settat",True]
mylist2[1]=1
mylist2[-1]=False
print(mylist2)
mylist2[0:3]=["a","b","c"]
print(mylist2)
mylist2[0:3]=[]
print(mylist2)
mylist2[0:3]=["tabi",19 ]
print(mylist2)
