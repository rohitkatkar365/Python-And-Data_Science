class Student:

    def __init__(self,name,cname,cp):
            self.name = name
            self.cname = cname
            self.lap = self.Laptop(cp)
    
    def show(self):
          print(self.name +" "+self.cname)
    
    class Laptop:
          
          def __init__(self,cp):
                self.cp = cp
        
          def show(self):
                print(self.cp)

s1 = Student("Rohit","ABC","HP")
s1.show()
s1.lap.show()