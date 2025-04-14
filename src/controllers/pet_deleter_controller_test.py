from .pet_deleter_controller import PetDeleterController # type: ignore
       
def test_delete(mocker):
    mock_repository = mocker.Mock()
    controller = PetDeleterController(mock_repository)
    controller.delete("Fluffy")

    mock_repository.delete_pets.assert_called_once_with("Fluffy")
