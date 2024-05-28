from PNJ import PNJ 
class PNJ_amical(PNJ):
    def __init__(self,nom,dialogue):
        super().__init__(nom)
        self.dialogue = dialogue

    def Parler(self):
        print(self.dialogue)
