# ------------------------
# tuples
# [1]: tuples ecrire dans une parntheses 
# [2]: you can write tuples with out parantheses
# [3]:  tuple are order, to use index to acces item
# [4]: tuple are immutble => you cant add and delete 
# [5]: tuple items is note unique 
# [6]: tuple can have deferent data type 
# [7]:operators used in string and list availbele in tuples 
# -----------------------

# tuple syntex :
tupleone=("elmehdi","tabi")
tupletwo="elmehdi","tabi"
print(type(tupleone))
print(type(tupletwo))

# indexing 
tuplethree=(1,2,3,4,5)
print(tuplethree[0])
print(tuplethree[-1])
print(tuplethree[-3])


#  tuple  assignment
tuplefoor=(1,2,3,4,5)
# tuplefoor[2]="two"
# print(tuplefoor)  'tuple' object does not support item assignment  

tuplefive=("elmehdi" , "elmehdi" ,1 ,2 ,100 ,112.2, False)
print(tuplefive[1])
print(tuplefive[-1])
print(tuplefive[-2])
print(len(tuplefive))

test=("ms" ,"ibm" ,"apple" , 10 , 15 , 15.5)
a=test[0]*2
print(a)
b=test[-3]%test[-2]
print(b)




print("#"*50)

tb = (1,56,8,9,6,4,5)
print(tb[1:])