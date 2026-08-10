import logging

logger = logging.getLogger(__name__)


class HybridValidator:

    @staticmethod
    def assert_user_flow(api_user, db_user, expected_user_id):
        """
        Validate that each layer successfully returned the expected user.
        """

        # API validation
        assert api_user is not None, "API did not return a user."
        assert api_user["id"] == expected_user_id, (
            f"Expected API user ID {expected_user_id}, "
            f"but got {api_user['id']}."
        )

        # Database validation
        assert db_user is not None, "Database did not return a user."
        assert db_user["id"] == expected_user_id, (
            f"Expected database user ID {expected_user_id}, "
            f"but got {db_user['id']}."
        )

        logger.info(
            "Hybrid validation passed for user ID %s.",
            expected_user_id
        )

    @staticmethod
    def assert_cart_product(cart_page, product_name):
        """
        Validate that the expected product is present in the cart.
        """

        assert cart_page.has_product(product_name), (
            f"Product '{product_name}' was not found in the cart."
        )

        assert cart_page.get_product_count() > 0, (
            "The shopping cart is empty."
        )

        logger.info(
            "Product '%s' is present in the cart.",
            product_name
        )

    @staticmethod
    def assert_cart_product_details(cart_page, product):
        """
        Validate the product name and price displayed in the cart.
        """

        product_name = product["name"]
        expected_price = product["price"]

        actual_name = cart_page.get_product_name(product_name)
        actual_price = cart_page.get_product_price(product_name)

        assert actual_name == product_name, (
            f"Expected product name '{product_name}', "
            f"but got '{actual_name}'."
        )

        actual_price = float(actual_price.replace("$", ""))

        assert actual_price == expected_price, (
            f"Expected price {expected_price}, "
            f"but got {actual_price}."
        )

        logger.info(
            "Product '%s' name and price validated successfully.",
            product_name
        )
