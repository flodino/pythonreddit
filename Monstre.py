from PNJ import PNJ

class Monstre(PNJ):
    def __init__(self,nom,attaque,pv_Maximum) -> None:
        super().__init__(nom)
        self.attaque = attaque
        self.pv_Maximum = pv_Maximum
        self.pv = self.pv_Maximum
        

    def attaquer(self,cible):
        cible.recevoir_degats(self.attaque)



    def recevoir_degat(self,degats):
        self.pv -= degats
        if(self.pv <= 0):
            self.mort()

    def mort():
        print("Vous avez vaincu",Monstre.nom)
        