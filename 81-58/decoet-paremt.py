def mondecor (func) :  #decorators 
    def nestedfun(n1,n2) :  
        if n1 < 0 or n2< 0 :
          print("une au deux nombre inferier a  0 ")
        func(n1,n2) #exuxted function
    return nestedfun
def decordeux(num) : 
    def decor(n,n1) :
        print ("j'avai en le decore deux de la page : " )
        num(n,n1)
    return decor
@decordeux
@mondecor
def calc (n1,n2) : 
    print(n1+n2)
calc(80,90)