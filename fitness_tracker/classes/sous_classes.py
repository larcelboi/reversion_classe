from .robot import Robot
from fitness_tracker.type_enum.enum_mode import Mode

class Drone(Robot):
    def __init__(self, name: str, speed: int, mode: Mode, mision_active: bool,altitude:int):
        super().__init__(name, speed, mode,mision_active)
        self.altitude = altitude

    @property
    def altitude(self):
        return self._altitude
    @altitude.setter
    def altitude(self,nouv_altitude):
        if isinstance(nouv_altitude,int):
            self._altitude = nouv_altitude
        else:
            raise ValueError('altitude must be an integer')

    def ascend(self):
        pass

    def decscend(self):
        pass

    def start_mission_drone(self):
        if self.altitude < 10:
            raise RuntimeError('cannot star mission. Altitude is lower then 10')
        else:
            self.start_mission()

    def __str__(self):
        return super().__str__() + f" Altitude: {self.altitude}"

class Groundrobot(Robot):
    def __init__(self, name: str, speed: int, mode: Mode, mision_active: bool):
        super().__init__(name, speed, mode,mision_active)
