class Distance:

    # коэффициент в метрах
    _conversion = {'mm': 0.001 , 'cm': 0.01 , 'm': 1 , 'km': 1000 ,}

    def __init__(self, value: float , unit: str = 'm'):
        if unit not in self._conversion:
            raise ValueError(f'Недопустимое значение: {unit}')
        self.value = value
        self.unit = unit

    def __str__(self):
        return f'{self.value} {self.unit}'

    def to_meters(self):
        return self.value * self._conversion[self.unit]

    def _convert_value(self, meters: float , target_unit: str) -> float:
        return meters / self._conversion[target_unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() + other.to_meters()
        new_value = self._convert_value(total_meters, self.unit)
        return Distance(new_value, self.unit)


    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        diff_meters = self.to_meters() - other.to_meters()
        if diff_meters < 0:
            raise ValueError('Результаты не могут быть отрицательными')
        new_value = self._convert_value(diff_meters, self.unit)
        return Distance(new_value, self.unit)

    # методы сравнения

    def __eq__(self, other):
        return self.to_meters() == other.to_meters()


    def __lt__(self, other):
        return self.to_meters() < other.to_meters()


    def __gt__(self, other):
        return self.to_meters() > other.to_meters()


    def __le__(self, other):
        return self.to_meters() <= other.to_meters()


    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()

























