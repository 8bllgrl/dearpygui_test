from abc import ABC, abstractmethod


class TabInterface(ABC):
    @abstractmethod
    def create(self):
        pass
