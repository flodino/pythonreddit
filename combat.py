from heros import heros
from initialisation import classesPossibles, Zones,Villageois1,Villageois2 
from Monstre import Monstre
from object import object
from  PNJ import PNJ
from PNJ_amical import PNJ_amical
import time 

class combat:
    def __init__(joueur,monstre):
        if(monstre.attaque > joueur.attaque):
            while(monstre.pv > 0 or joueur.pv):
                monstre.attaquer(joueur)
                time.sleep(1)
                print("pv du joueur :",joueur.pv)
                joueur.attaquer(monstre)
                print("pv du monstre:",monstre.pv)
                if(joueur.pv >0):
                    vainqueur = joueur
                elif (monstre.pv >0):
                    vainqueur = monstre 
        
        else: 
            while(monstre.pv > 0 or joueur.pv):
                joueur.attaquer(monstre)
                print(monstre.pv)
                monstre.attaquer(joueur)
                print("pv du joueur :",joueur.pv)
                if(joueur.pv >0):
                    vainqueur = joueur
                elif (monstre.pv >0):
                    vainqueur = monstre 
        combat.fin_de_combat(vainqueur)
        return vainqueur
    
    def fin_de_combat(self, vainqueur):
        print("Le Vainqueur est:",vainqueur)
        

                

