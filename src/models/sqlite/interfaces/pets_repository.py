from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pets import Pet


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> List[Pet]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass
