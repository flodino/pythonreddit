import sys 
from dataclasses import dataclass
from inventaire import inventaire
@dataclass
class heros:
        nom : str
        classe : str 
        attaque : int 
        inventaire : inventaire
        niveau : int = 1
        lieuActuel : str ="Madrigal"
        Competences : list | None = None
        pv_Maximum : int = 100
        pv : int = 100
    

        def attaquer(self,cible):
                cible.recevoir_degats(self.attaque)


        def recevoir_degat(self,degats):
                self.pv -= degats
                if(self.pv <= 0):
                        self.mort()

        def mort(self):
                print("Vous avez été vaincu")
                sys.exit()

        def ajouter_objet(self,objet):
                inventaire.ajouter_objet(self,objet)
    

        def enlever_objet(self,objet):
                inventaire.enlever_objet(self,objet)




    
        
        
