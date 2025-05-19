from device import Device
from type_enum.type_device import Device_type


class Light(Device):
    def __init__(self,name,type_vechile:Device_type,status,brightness):
        super().__init__(name,type_vechile,status)
        self.brightness = brightness

    @property
    def brightness(self):
        return self._brightness
    @brightness.setter
    def brightness(self,nouv_brightness):
        if isinstance(nouv_brightness,int) and nouv_brightness in range(0,101):
            self._brightness = nouv_brightness
        else:
            raise ValueError("brightness must be between 0 and 100")

    def set_brightness(self,brightness):
        self._brightness = brightness
    def __str__(self):
        return super().__str__() + f" Brightness: {self.brightness}"

class Thermostat(Device):
    def __init__(self,name,type_vechile:Device_type,status,temperature):
        super().__init__(name,type_vechile,status)
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, nouv_temperature):
        if isinstance(nouv_temperature, int) and nouv_temperature in range(10, 31):
            self._temperature = nouv_temperature
        else:
            raise ValueError("brightness must be between 0 and 31")

    def set_temperature(self,temperature):
        self._temperature = temperature

    def __str__(self):
        return super().__str__() + f" Tempature: {self.temperature}"

class Camera(Device):
    def __init__(self, name, type_vechile: Device_type, status,is_recording):
        super().__init__(name, type_vechile, status)
        self.is_recording = is_recording

    @property
    def is_recording(self):
        return self._is_recording

    @is_recording.setter
    def is_recording(self, nouv_is_recording):
        if isinstance(nouv_is_recording, bool):
            self._is_recording = nouv_is_recording
        else:
            raise ValueError("is_recording must be a bool true or false")

    def toggle_recording(self,recording):
        self._is_recording = not recording
    def __str__(self):
        return super().__str__() + f" Recording: {"ON"if self.is_recording else "OFF"}"