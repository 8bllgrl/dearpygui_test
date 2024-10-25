from abc import ABC, abstractmethod


class TabInterface(ABC):
    @abstractmethod
    def draw(self):
        pass
