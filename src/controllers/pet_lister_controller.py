from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable # type: ignore
from .interfaces.pet_lister_controller import PetListerControllerInterface # type: ignore

class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository:PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets
    
    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_response = []
        for pet in pets:
            formatted_response.append({"name": pet.name, "type": pet.type, "id": pet.id})
        
        return {
            "data":{
                "type": "Pets",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
    