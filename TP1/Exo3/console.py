from Exo1 import Operateur
from Exo2 import DataTrans
try :
    exo=int(input("Quelle exercice souhaite vous resoudre : tapez 1 pour l'exo1 , 2 pour l'exo2  :"))
    if exo==1:
        N=int(input("Donnez une valeur a l'entier N :"))
        liste1=Operateur(N)
        print("La liste est ",liste1.liste())
        print("La valeur de R est ", liste1.calculR())
    elif exo==2:
        n=int(input("donnez le nombre de liste :"))
        s=int(input("donnez le nombre d'element de chaque liste :"))       
        Liste=DataTrans(n,s)
        Liste.img()
    else :
        exit()
except error :
        print(error)