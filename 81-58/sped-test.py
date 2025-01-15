# def mondecor (func) :  #decorators 
#     def nestedfun(*num) : 
#         for nmb in num :  
#          if nmb< 0 :
#            print("une au deux nombre inferier a  0 ")
#         func(*num) #exuxted function
#     return nestedfun
# @mondecor
# def calc (n1,n2,n3,n4,n5) : 
#     print(n1+n2++n4+n3+n5)
# calc(80,90,90,4,8,)

from time import  time 

def temp(tm) : 
    def wraper() : 
        start = time ()
        tm ()
        end= time()
        print( f"function est travaille depuis :{(end - start)}")
    return wraper 
@temp
def caltemps () : 
    for i in range(1,200000) :
       print(i)
caltemps ()