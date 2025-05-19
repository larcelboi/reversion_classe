from normal.vehicule_type.type_vehicule import Type_vehicule

class Vehicule:
    def __init__(self,name,type_vechile:Type_vehicule):
        self.name = name
        self.type_vechile = type_vechile

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,nouv_name):
        if isinstance(nouv_name,str) and nouv_name.strip() != "":
            self._name = nouv_name
        else:
            raise ValueError("Name cannot be empty")

    @property
    def type_vechile(self):
        return self._type_vechile

    @type_vechile.setter
    def type_vechile(self,nouv_type_vechile:Type_vehicule):
        if isinstance(nouv_type_vechile,Type_vehicule):
            self._type_vechile = nouv_type_vechile
        else:
            raise ValueError("Type voiture must be of type Vechile")

    def __str__(self):
        return f"Nom: {self.name} Type vehicule: {self.type_vechile.value}"