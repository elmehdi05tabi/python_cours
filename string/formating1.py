# formating à l'boc
name="elmehdi"
age=19
cp=22
print("my name is :"+name)
# print("may name is :"+name+"and my age is "+age) => error
print("my name is :%s and my age is:%d my code postale is:%f" %(name,age,cp))

# %s => string
# %d => numbre
# %f => float 

# changer le nombre de zero en %f 

a=20
print("mon score est %.2f" %(a))
print("mon score est %.4f" %(a))

#truncite string 
a2="je vais bien et vous "
print ("bonjour mon ami comment tu-vas %.12s" %(a2))