from dataclasses import dataclass
@dataclass
class inventaire: 
  objets : list | None = None
  
  def ajouter_objet(self,caller,objet):
        self.objets.append(objet)
        objet.prise_effet(caller)

      #  emplacement = None 
        # for X in range(len(self.objets)):
          #  if self.objects[X].nom == objet:
           #     emplacement = X
             #   self.objets[emplacement].prise_effet(caller)
        
        

  def enlever_objet(self,caller,objet):
        emplacement = None
       # for X in range(len(self.objets)):
        #    if self.objects[X].nom == objet:
         #       emplacement = X
          #      self.objets[emplacement].enlever_effet(caller)
        self.objets.append(objet)
        objet.enlever_effet(caller)
       

    
        
    


