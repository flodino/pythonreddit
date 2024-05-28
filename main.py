from heros import heros
from initialisation import classesPossibles, Zones,Villageois1,Villageois2,objet1
from Monstre import Monstre
from  PNJ import PNJ
from PNJ_amical import PNJ_amical
from inventaire import inventaire
import time 

print("Bonjour Heros \n  Quel est votre nom ")
nom = input("Votre nom ? ")
print("Très bien",nom,"Bienvenue au sein de votre premier jeu vidéo")
print("Quelle classe souhaitez vous avoir ?")
for x in range(len( classesPossibles)):
    print(classesPossibles[x], end=",")
ResponseClass = None 
while (ResponseClass == None) :
    ResponseClass = input("\n Votre classe? ")
    if ResponseClass in classesPossibles:
        print("Votre classe sera donc ",ResponseClass)
        # time.sleep(2)
    else:
        ResponseClass= None
if ResponseClass == "Magicien":
    herosPrincipal = heros(nom,ResponseClass,10,inventaire() )
elif ResponseClass == "Guerrier":
    herosPrincipal = heros(nom,ResponseClass,18,inventaire())
print("Félicitations vous êtes dans la première zone",herosPrincipal.lieuActuel)
# time.sleep(2)
print(Villageois1.nom,":",end=(""))
Villageois1.Parler()
ResponseChoice0 = None
while(ResponseChoice0 == None):
    ResponseChoice0 = input("Souhaitez vous aller à la maison évoquée ? \n A - Oui, B-Non ")
    if(ResponseChoice0 == "A"):
        herosPrincipal.lieuActuel="Maison_1"
    else:
        ResponseChoice0= None
print("Vous êtes arrivés dans la maison 1")
Villageois2.Parler()
print(herosPrincipal)
herosPrincipal.ajouter_objet(objet1)
print(herosPrincipal)












        








