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

    @staticmethod
    def assert_checkout_totals(overview_page):
        """
        Validate subtotal, tax and total displayed in checkout overview.
        """

        product_prices = overview_page.get_product_prices()
        subtotal = overview_page.get_item_total()
        tax = overview_page.get_tax()
        total = overview_page.get_total()

        expected_subtotal = round(sum(product_prices), 2)

        assert subtotal == expected_subtotal, (
            f"The subtotal of the UI ({subtotal}) does not match "
            f"the sum of its products ({expected_subtotal})."
        )

        expected_tax = round(subtotal * 0.08, 2)

        assert tax == expected_tax, (
            f"The tax calculated by the system ({tax}) "
            f"is not the expected 8% ({expected_tax})."
        )

        expected_total = round(subtotal + tax, 2)

        assert total == expected_total, (
            f"The final total of the UI ({total}) does not equal "
            f"subtotal + tax ({expected_total})."
        )

        logger.info(
            "Checkout totals validated successfully. "
            "Subtotal: %s, Tax: %s, Total: %s",
            subtotal,
            tax,
            total
        )

    @staticmethod
    def assert_inventory_loaded(inventory_page):
        assert inventory_page.is_loaded(), (
            "Inventory page was not loaded."
        )


    @staticmethod
    def assert_product_in_catalog(inventory_page, product):
        product_names = inventory_page.get_all_product_names()

        assert product["name"] in product_names, (
            f"Product '{product['name']}' was not found in the catalog."
        )


    @staticmethod
    def assert_product_price(inventory_page, product):
        actual_price = inventory_page.get_product_price(
            product["name"]
        )

        actual_price = float(
            actual_price.replace("$", "")
        )

        assert actual_price == product["price"], (
            f"Expected price {product['price']}, "
            f"but got {actual_price}."
        )


    @staticmethod
    def assert_cart_badge(inventory_page, expected_count):
        actual_count = inventory_page.get_cart_badge_count()

        assert actual_count == expected_count, (
            f"Expected cart badge to be {expected_count}, "
            f"but got {actual_count}."
        )
