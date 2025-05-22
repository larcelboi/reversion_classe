from fitness_tracker.type_enum.enum_mode import Mode

class Robot:
    _liste_erreur = []
    def __init__(self,name: str,speed: int,mode: Mode,mision_active: bool):
        self.name = name
        self.speed = speed
        self.mode = mode
        self.mision_active = mision_active
        self.status = "Active"if self.mision_active else "Inactive"

    def erreur_name(self,nouv_name):
        try:
            if isinstance(nouv_name, str) and nouv_name.strip() != "":
                self._name = nouv_name
            else:
                raise ValueError("Name must be a string and contain a name")
        except Exception as e:
            Robot._liste_erreur.append(e)

    def erreur_speed(self,nouv_speed):
        try:
            if isinstance(nouv_speed, int) and nouv_speed in range(0, 101):
                self._speed = nouv_speed
            else:
                raise ValueError("speed must be a float between 0 and 100")
        except Exception as e:
            Robot._liste_erreur.append(e)

    def erreur_mode(self,nouv_mode):
        try:
            if isinstance(nouv_mode, Mode):
                self._mode = nouv_mode
            else:
                raise ValueError("mode must be a Mode")
        except Exception as e:
            Robot._liste_erreur.append(e)


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,nouv_name):
       self.erreur_name(nouv_name)

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self,nouv_speed):
        self.erreur_speed(nouv_speed)

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self,nouv_mode):
        self.erreur_mode(nouv_mode)


    def start_mission(self):
        try:
            if not self.mision_active:
                self.mision_active = True
                self.status = "Active"
            else:
                raise RuntimeError(f"Le robot {self.name} est déjà en mission ")
        except Exception as e:
            Robot._liste_erreur.append(e)

    def emergency_stop(self):
        self.mision_active = False
        self.speed = 0

    def apply_settings(self,speed,mode:Mode):
        self.speed = speed
        self.mode = mode

    def __str__(self):
        return f"Nom : {self.name} Speed: {self.speed} Mode: {self.mode.value} Mission {self.status}"