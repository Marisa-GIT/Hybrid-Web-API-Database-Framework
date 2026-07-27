class UserSchemas:
        USER_SCHEMA_KEYS = {
            "id": int,
            "name": str,
            "username": str,
            "email": str,
            "address": dict,   
            "phone": str,
            "website": str,
            "company": dict   
        }
        
class ResponseValidator:

    @staticmethod
    def assert_status_code(response, expected_code=200):
        assert response.status_code == expected_code, (
            f"Expected status code {expected_code}, but received a {response.status_code}"
        )

    @staticmethod
    def assert_not_empty_list(data):
        assert isinstance(data, list), (
            f"A list was expected, but it was obtained {type(data).__name__}"
        )
        assert len(data) > 0, "The received list is empty."

    @staticmethod
    def assert_user_schema(user_data):
        assert isinstance(user_data, dict), "The user object must be a dictionary."
        
        from api.response_validator import UserSchemas
        
        for field, expected_type in UserSchemas.USER_SCHEMA_KEYS.items():
            
            assert field in user_data, (
                f"The required field '{field}' is missing in the user. "
                f"Fields present: {set(user_data.keys())}"
            )
            
            
            actual_value = user_data[field]
            assert isinstance(actual_value, expected_type), (
                f"Incorrect data type for the field '{field}'. "
                f"Expected {expected_type}, but received {type(actual_value).__name__} (Value: {actual_value})"
            )
    @staticmethod
    def assert_user_id(user_data, expected_id):
        assert user_data.get("id") == expected_id, (
            f"The ID was expected {expected_id}, but received {user_data.get('id')}"
        )