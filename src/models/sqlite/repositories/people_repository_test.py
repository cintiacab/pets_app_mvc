from unittest import mock
from pytest import raises
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from .people_repository import PeopleRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data =[
                ( # Mock query for PeopleTable
                    [mock.call.query(PeopleTable)], 
                    [
                       PeopleTable(id=1, first_name= "Carol", last_name= "Silva", age= 28, pet_id= 1),
                       PeopleTable(id=2, first_name= "Ana", last_name= "Maria", age= 45, pet_id= 2)
                    ] # query result 
                ),
                ( # Mock query for PetsTable
                    [mock.call.query(PetsTable)],
                    [
                       PetsTable(id=1, name="dog", type="dog"),
                       PetsTable(id=2, name="cat", type="cat")
                   ]
                ),
            ]
        )

    def __enter__(self): 
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        pass

class MockConnectionException:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.add.side_effect = self.__raise_exception

    def __raise_exception(self, *args, **kwargs):
        raise Exception("Error")

    def __enter__(self): 
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No Result Found")

    def __enter__(self): 
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        pass

def test_insert_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)
    
    repo.insert_person("test name", "test last", 50, 3)

    mock_connection.session.query.assert_not_called()
    mock_connection.session.add.assert_called_once()

def test_insert_person_error():
    mock_connection = MockConnectionException()
    repo = PeopleRepository(mock_connection)

    with raises(Exception):
        repo.insert_person("test name", "test last", 50, 3)
    
    mock_connection.session.rollback.assert_called_once()

def test_get_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)

    repo.get_person(1)

    mock_query = mock_connection.session.query.return_value
    mock_outerjoin = mock_query.outerjoin.return_value
    mock_filter = mock_outerjoin.filter.return_value
    mock_with_entities = mock_filter.with_entities.return_value

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_query.outerjoin.assert_called_once_with(PetsTable, PetsTable.id == PeopleTable.pet_id)
    mock_outerjoin.filter.assert_called_once_with(PeopleTable.id == 1)
    mock_filter.with_entities.assert_called_once_with(
                                                        PeopleTable.first_name,
                                                        PeopleTable.last_name,
                                                        PetsTable.name.label("pet_name"),
                                                        PetsTable.type.label("pet_type")
                                                        )
    mock_with_entities.one.assert_called_once()

def test_get_person_no_result():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)

    person = repo.get_person(1)

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    assert person is None
