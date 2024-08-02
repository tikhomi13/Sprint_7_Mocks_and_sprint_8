import requests
from unittest.mock import Mock, patch


class User:

    def __init__(self, data):
        self.user = data

    def get_user_details(self, user_id):
        response = requests.get('http://some-account-uri/' + user_id)
        return {'status': response.status_code, 'data': response.text}


class TestUser:

    @patch('user.requests')  # (2)
    def test_get_current_user_details(self, mock_requests):  # (3)
        mock_response = Mock()  # (4)
        mock_response.status_code = 200
        mock_response.text = 'User data'
        mock_requests.get.return_value = mock_response  # (5)

        user = User(mock_response)  # (6)
        assert {'status': 200, 'data': 'User data'} == user.get_user_details('1')  # (7)


# Задача теста — проверить метод get_user_details() без обращения к сервису.

# Сначала нужно импортировать класс User и инструменты из модуля unittest.mock

# Следующим действием создадим тест и навесим на него декоратор @patch

# Он должен замокировать модуль requests (то есть отправку ГЕТ-запроса)

# Если этого не сделать, метод будет вызывать настоящий метод get() и отправлять запрос

# Передаём в тест мок в качестве параметра.

# Получился путь 'user.requests'.
# Декоратор прочитает его так: замени импорт модуля requests в файле `user.py'

# from unittest.mock import Mock, patch   # (1)

# from user import User

# class TestUser:

#    @patch('user.requests')   # (2)  ПОДМЕНА ЗАПРОСА (импорта модуля)
#    def test_get_current_user_details(self, mock_requests):  # (3)

        # Теперь во время теста код будет вызывать методы из мока, а не из модуля requests.

        # Теперь нужно Настроить мок mock_requests

        # Его метод get() должен сымитировать запрос и ответ сервиса.

        # Метод get_user_details возвращает объект данных

        # У этого объекта данных есть атрибуты status_code и text

        # Значит, нужно создать мок с такими же атрибутами и передать его в кач-ве возвращаемого значения

        # Для этого.

        # 1) Создаем мок mock_response

        # 2) Устанавливаем ему атрибуты status_code и text

        # 3) Указываем его (мок?) в кач-ве возвращаемого значения метода get() - это где return_value

        # Итак. Создали мок mock_response и устанавливили ему атрибуты status_code и text.

        # Указываем его в качестве ВОЗВРАЩАЕМОГО ЗНАЧЕНИЯ метода get() объекта mock_requests. это где return_value (дубль)






# Далее. Создаем пользователя - то есть объект класса User. Объект принимает инфу о пользователе

# Поэтому передаем ему мок с данными - mock_response (объект кл. Mock, см код выше )

# Последний шаг теста — это проверка. С помощью ассерта убеждаемся, что метод ...

# ... user.get_user_details возвращает информацию, которая соответствует эталону



# единица - это айди (похоже может быть любой)









