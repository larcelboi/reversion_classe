from type_enum.type_device import Device_type


class Device:
    def __init__(self,name,type_vechile:Device_type,status):
        self.name = name
        self.type_vechile = type_vechile
        self.status = status if status else False
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, nouv_name):
        if isinstance(nouv_name, str) and nouv_name.strip() != "":
            self._name = nouv_name
        else:
            raise ValueError("nom must be a string and contain something")
    @property
    def type_vechile(self):
        return self._type_vechile

    @type_vechile.setter
    def type_vechile(self, nouv_type_vechile):
        if isinstance(nouv_type_vechile, str):
            self._type_vechile = nouv_type_vechile
        else:
            raise ValueError(f"{nouv_type_vechile} must be a Type_vehicule")
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, nouv_status):
        if isinstance(nouv_status, bool):
            self._status = nouv_status
        else:
            raise ValueError("Status must be a bool true  or false")

    def __str__(self):
        return f"Nom: {self.name} Type: {self.type_vechile} Status: {"ON" if self.status else "OFF"}"
            