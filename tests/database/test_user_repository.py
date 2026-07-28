from database.validators import DatabaseValidator


class TestUserRepository:
    """Test suite for UserRepository."""

    def test_get_all_users(self, user_repository):
        """Verify that all users can be retrieved."""

        users = user_repository.get_all_users()

        DatabaseValidator.assert_not_empty_list(users)

        DatabaseValidator.assert_user_schema(users[0])

    def test_get_user_by_id(self, user_repository):

            """Verify retrieving an existing user by ID."""


            user_id = 1


            user = user_repository.get_user_by_id(user_id)


            DatabaseValidator.assert_user_exists(user)

            DatabaseValidator.assert_user_id(user, user_id)

            DatabaseValidator.assert_user_schema(user)

    def test_get_user_not_found(self, user_repository):

        """Verify querying a non-existent user."""


        user = user_repository.get_user_by_id(9999)


        assert user is None

    def test_user_exists(self, user_repository):

            """Verify that an existing user is found."""


            assert user_repository.user_exists(1) is True


    def test_user_does_not_exist(self, user_repository):

        """Verify that a non-existent user is not found."""


        assert user_repository.user_exists(9999) is False