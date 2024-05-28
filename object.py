from dataclasses import dataclass


@dataclass
class object:
    type : str
    nom  : str
    effet_type : str
    effet_nombre : int

    def prise_effet(self,caller):
        if(self.effet_type== "augmente_attaque"):
            caller.attaque += self.effet_nombre

    def enlever_effet(self,caller):
        if(self.effet_type== "augmente_attaque"):
            caller.attaque -= self.effet_nombre

            

    


        