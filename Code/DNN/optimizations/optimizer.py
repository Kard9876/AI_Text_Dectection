from abc import ABCMeta, abstractmethod


class Optimizer(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, *args):
        pass
