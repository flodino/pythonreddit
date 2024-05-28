from  PNJ import PNJ
from PNJ_amical import PNJ_amical
from heros import heros
from Monstre import Monstre
from inventaire import inventaire
from object import object


classesPossibles = ("Magicien","Guerrier")
Zones = ("Madrigal","Maison_1","Zone des Aibatts","Saint City","Shop_Saint_City","Maison_2")
# Dans le shop vendre potions 

Villageois1 = PNJ_amical("Professeur","Tu es le bienvenue dans ce joli village \n il faudrait que tu ailles dans cette première maison \n pour qu'un villageois te parle !")
Villageois2 = PNJ_amical("Villageois_Maison_1","Veux tu une épée ? Tiens la voici ! ")

Monstre1 = Monstre("Aibatt1",10,20)
objet1 = object("épée","épée en bois","augmente_attaque",10)


