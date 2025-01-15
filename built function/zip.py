#  ------------------------------------------------
# --- Practical => loop on many iterators with Zip()
#  ------------------------------------------------
# Zip () return a zip object contains all objects 
# Zip () length is the length of lowest object 
#  ------------------------------------------------
list1 = [1,2,3,4,5]
list2 = ["A","B","C"]
tuple1 = ("Homme","Famme","Garçon","Fille")
dict1 = {"Name":"elmehdi","Age":19,"Pays":"Maroc","Competance" : "Python"}

for item1 ,item2 ,item3,item4 in zip(list1,list2,tuple1,dict1) : 
    print("élement  dans list 1 => ",item1)
    print("élement  dans list 2 => ",item2)
    print("élement  dans tuple 1 => ",item3)
    print("key  dans dic 1 => ",item4,  " value est => ",dict1[item4])


























# mylsit = zip(list1 , list2)
# for item1,item2 in mylsit : 
#     print("elemnt dans la list 1 : ",item1)
#     print("elemnt dans la list 2 : ",item2)