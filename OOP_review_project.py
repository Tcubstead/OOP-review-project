#Thomas Cubstead
#OOP Review Project
#Shapes_Hierarchy
#9/21/25

import math
from abc import ABC, abstractmethod

class BasicShape(ABC):
    def __init__(self, name="shape"):
        self.area = 0.0
        self.name = name

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    @abstractmethod
    def calc_area(self):
        pass


