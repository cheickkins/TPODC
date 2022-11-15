import math
class Operateur :
    def __init__(self, n) :
        self.n=n
        
    def  liste(self):
        try:      
            if self.n>0:       
                return list(range(-self.n,self.n+1))
            else:
                print("La valeur donnee n'est pas un entier naturel")
        except TypeError:
            print("La valeur donnee n'est pas un entier naturel")
    def f(self,x) :
        return x/(x**2+1)
    def g(self,x) :
        return math.atan(x)
    
    def calculR(self):
        return sum([(self.f(x)-self.g(x))**2 for x in self.liste()])

  
    