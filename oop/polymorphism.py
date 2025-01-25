# ---------------------------------------------------------------
#&-- object oriented programming => Polymorphism 
# ---------------------------------------------------------------
n1 = 10 
n2 = 20 
print(n1 + n2)
s1 = "hello"
s2 = " python"
print(s1 + s2)

print(len([1,2,3,4,5,6,]))
print(len("hello elmehdi"))
print(len({"key_one":1,"key_two":2}))


class a : 
    def do_semting (self) : 
        print("from class a ")
        raise NotImplementedError ("ta 3armha asahbi ")

class b(a) : 
  def do_semting (self) : 
        print("from class b ")
class c(a) : 
    def do_semting (self) : 
        print("from class c  ")
my_inst = c() 
my_inst.do_semting()