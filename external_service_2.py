import requests
from unittest.mock import Mock, patch   # (1)


class User:

    def __init__(self, database):
        self.database = database

    def get_user_details(self, user_id):
        return self.database.get_user_details(user_id)


class Database:

    def get_user_details(self, user_id):
        # эмулируем запрос к базе данных
        # в реальном приложении здесь будет логика запроса к БД
        if user_id == '1':
            return {'data': 'User data'}
        else:
            return {'data': 'User not found'}


class TestUser:

    @patch('user.Database')
    def test_get_current_user_details(self, mock_database_class):

        mock_database = Mock()
        mock_database.text = {'data': 'User data'}
        mock_database_class.return_value = mock_database
        user = User(mock_database)

        assert {'data': 'User data'} == user.get_user_details(1)


        # assert user.get_user_details() == mock_database.text
        # assert user.get_user_details(1) == {'data': 'User data'}
