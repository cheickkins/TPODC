import random
import math
class DataTrans :
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def list_composee(self) :
        liste=[]
        for i in range(self.n) :
            elt_list=random.sample(range(1,20), self.s)
            liste.append(elt_list)
        return liste   
    def f(self, x):
            return x**3+3*(x**2)-5
    
    def img(self):
        lis=self.list_composee()
        mx=[]
        mn=[]
        for i in lis:    
            mi=i[0]
            ma=i[0]
            for j in range(len(i)) :
                if i[j]>ma :
                    ma=i[j]
                if i[j]<mi :
                    mi=i[j]
            mx.append(ma)
            mn.append(mi)
        print("la liste D est :",lis)
        print("liste des maximums :",mx)
        print("liste des minimums:",mn)
        print("le maximum global est :",max(mx))
        print("le minimum global est :",min(mn))
        liste=[]
        lit=[]
        for i in lis:
            for j in range(len(i)) :
                lit.append(self.f(i[j]))
            liste.append(lit)
        print("L'image de la liste est :", liste)
            
                
            
        
        
        
    