
# ----------------------------------

# append() => ajoute un élement dans le list  
# elle est ajouté list en  list 

# ----------------------------------


myfirstlist=["elmehdi","tabi",19,"settat","morocco"]
mysecondlist=["nezha","mjid","asmaee"] 
print(myfirstlist) #["elmehdi","tabi",19,"settat","morocco"]
myfirstlist.append("ma mére") 
print(myfirstlist)#  ["elmehdi","tabi",19,"settat","morocco" ,"ma mére" ]
myfirstlist.append(mysecondlist) 
print(myfirstlist) #["elmehdi","tabi",19,"settat","morocco" ,"ma mére" ,["nezha","mjid","asmaee"] ]
print(myfirstlist[5]) #ma mére
print(myfirstlist[6]) #["nezha","mjid","asmaee"] 
print(myfirstlist[6][-1]) # la dernier élment en list 2 => asmaee 


#-------------------------------------

#extend() => ajoute un élement dans le list 
#    
#----------------------------
a=[1,2,3]
b=["a","b","c"]
c=["one","two",False]
a.extend(b)
a.extend(c)
print(a)


#--------------------------------
# remove () => suprime les élment il commance par le premier elment dans le list 
#--------------------------------


k =["elmehdi" , "settat" ,"tabi","morocco" ,"tabi" ,"tabi"]
k.remove("tabi")
print(k)


#--------------------------------
# sort () => tri  
# sort (reverse=True) => tri en order inverse
# sort (reverse=False) => tri en order normal 
#--------------------------------
x=[15 , 30 ,-5 ,13 ,102 ,33 ,50 ]
x.sort()
print(x)
x.sort(reverse=True)
print(x)
y = ["h" , "c" ,"k" ,"a" ,"d"]
y.sort()
print(y)
y = ["elmehdi" , "saad" ,"anoir" ,"mohamed" ,"brahim"]
y.sort()
print(y)

# ---------------------------------
#  reverse => il est reverse list c'est tout 

# ---------------------------------

list1=[10,50 ,4 ,53 ,"elmehdi" ,99.2]
list1.reverse()
print(list1)

