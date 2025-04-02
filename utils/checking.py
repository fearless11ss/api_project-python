from requests import Response
import json

class Checking():

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Успешно, статус код {status_code}")
        else:
            print(f"Провал, статус код {status_code}")

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(response:Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"{field_name} верен")

    @staticmethod
    def check_json_search_word_in_value(response:Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f"Слово {search_word} присутствует")
        else:
            print(f"Слово {search_word} отсутствует")