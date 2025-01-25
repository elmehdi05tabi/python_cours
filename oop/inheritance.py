# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food : # base class
    def __init__(self,name,price) : 
        self.name = name
        self.price = price
        print(f"{self.name} is creat from base class and price is {self.price} ")
    def eat(self) : 
        print("eat method from base class ")
class Apple(Food) : # derive class 
    def __init__(self,name,price,etoil) : 
        # Food.__init__(self,name) # creat inistance form base class 
        super().__init__(name,price) 
        self.etoil = etoil
        print(f"{self.name} is creat from derived class the price is {self.price} je donne {self.etoil} ")
    def get_thre (self) : 
        print("je suis le meilleure chef dans le maroc acttulment :")
# food_one = Food ()
food_two =  Apple("tacos",35,2.5) 
food_two.eat()
food_two.get_thre () 