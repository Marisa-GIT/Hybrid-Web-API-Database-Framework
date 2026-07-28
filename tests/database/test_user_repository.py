from database.validators import DatabaseValidator
import pytest

VALID_USER_ID = 1
INVALID_USER_ID = 9999
class TestUserRepository:
    @pytest.mark.parametrize(
        "user_id, expected",
        [
            (VALID_USER_ID, True),
            (INVALID_USER_ID, False),
        ],
        ids=["user_exists", "user_does_not_exist"]
    )
    def test_user_exists(self, user_repository, user_id, expected):
        """Verify that user_exists returns correct status for existing and non-existing IDs."""
        assert user_repository.user_exists(user_id) is expected

    def test_get_all_users(self, user_repository):

        users = user_repository.get_all_users()

        DatabaseValidator.assert_not_empty_list(users)

        DatabaseValidator.assert_user_schema(users[0])

    def test_get_user_by_id(self, user_repository):

        user = user_repository.get_user_by_id(VALID_USER_ID)


        DatabaseValidator.assert_user_exists(user)

        DatabaseValidator.assert_user_id(user, VALID_USER_ID)

        DatabaseValidator.assert_user_schema(user)

    def test_get_user_not_found(self, user_repository):

        user = user_repository.get_user_by_id(INVALID_USER_ID)


        assert user is None, "Expected no user for a non-existent ID."
        



