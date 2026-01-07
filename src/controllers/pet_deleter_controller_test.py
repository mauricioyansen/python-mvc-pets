import src.controllers.pet_deleter_controller as PetDeleterController


def test_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetDeleterController.PetDeleterController(mock_repository)
    controller.delete("Buddy")

    mock_repository.delete_pets.assert_called_once_with("Buddy")
