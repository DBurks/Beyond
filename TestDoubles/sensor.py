import random

class Sensor:
    def __init__(self):
        pass

    def sample_pressure(self):
        """Provides a random pressure reading centered at 19 with 2 sigma.

        Examples
        --------
        >>> random.seed(42)
        >>> sensor = Sensor()
        >>> sensor.sample_pressure()
        18.711819340844144
        >>> sensor.sample_pressure()
        18.65419279933696
        >>> sensor.sample_pressure()
        18.777368276864674
        >>> sensor.sample_pressure()
        20.403967450197726
        >>> sensor.sample_pressure()
        18.744823432434227
        >>> sensor.sample_pressure()
        16.005293171318087
        >>> sensor.sample_pressure()
        19.66463668813543
        """
        return random.gauss(19, 2.0)

