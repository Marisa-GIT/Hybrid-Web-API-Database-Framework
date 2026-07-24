
import json 

class TestDataManager:

    @staticmethod
    def read_users():
        with open("data/users.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_user(user_type):
        return TestDataManager.read_users()[user_type]

    @staticmethod
    def get_product(product_key):

        with open("data/products.json", "r") as file:
            productos = json.load(file)

            if product_key in productos:
                return productos[product_key]
            
        raise KeyError(f"The key '{product_key}' does not exist in products.json")

    @staticmethod
    def get_specific_products(clavelist):

        with open("data/products.json", "r") as file:
            productos = json.load(file)
       
            return [productos[clave] for clave in clavelist if clave in productos]