# coding=utf-8
"""PWM wrapper for RPi.GPIO.PWM
"""
import RPi.GPIO as gpio

class PWM(gpio.PWM):
    """Wrapper for RPi.GPIO.PWM that allows querying state"""
    
    _duty_cycle = None  # type: float


    def __new__(cls, *args, **kwargs):
        instance = super(PWM, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, Pin,  Freq=100):
        """
        :param Pin: Pin Number according to gpio mode
        :param DutyCycle: duty cycle 0-100
        :param Freq: frequency in Hertz
        """
        self.status = "Stopped"
        self._duty_cycle = 0
        self._frequency = Freq
        self.pin = Pin
        self.start(0)

    @property
    def dutyCycle(self):
        return self._duty_cycle
    
    @dutyCycle.setter
    def dutyCycle(self, *args, **kwargs):
        if not self.status == "Running":
            self.start(*args)
        else:
            super(PWM, self).ChangeDutyCycle(*args)
        self._duty_cycle = args[0]

    def ChangeFrequency(self, *args, **kwargs):
        self.frequency = args[0]

    def ChangeDutyCycle(self, *args, **kwargs):
        self.dutyCycle = args[0]

    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, *args, **kwargs):
        if not self.status == "Running":
            self.start(0)
        super(PWM, self).ChangeFrequency(*args)
        self._frequency= args[0]

    def start(self, *args, **kwargs):
        self.status = "Running"
        self._duty_cycle = args[0]
        super(PWM, self).start(*args, **kwargs)

    def stop(self, *args, **kwargs):
        self.status = "Stopped"
        super(PWM, self).stop(*args, **kwargs)

    def cleanup(self):
        gpio.cleanup(self.pin)
        pass
    def __str__(self):
        return "<PWM Object: Stutus: %s, GPIO: %s, Duty Cycle: %s, Frequency: %s>", self.status,self.pin, \
               self._duty_cycle, self._frequency
    def __repr__(self):
        return self.__str__()