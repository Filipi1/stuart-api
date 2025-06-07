from abc import ABC, abstractmethod


class ApplicationService(ABC):
    @abstractmethod
    def process(self, *args, **kwargs):
        raise NotImplementedError("M�todo process deve ser implementado")
