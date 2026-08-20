#!/usr/bin/python3

# shebang tells your computer what language interpreter to use (python)

import requests

class EcommerceApp:

    def __init__(self):
        # special variable that decides if we keep running and looping
        self.running = True

        print("Welcome to MegaMart")
        # http request to get/save products
        self.products = self.retrieve_products()
        # activate main menu
        self.main_menu()

    def main_menu(self):
        print("Choose a product by its number to look at:")
        self.print_product_names()
        print("If you would like to exit type EXIT")

        while self.running:
            self.prompt_product_choice()

    def print_product_names(self):
        counter = 0
        # loop products to print name / index
        for product in self.products:
            print(f"{counter} - {product["name"]}")
            counter += 1
        # TODO: increase product number so it starts at 1 instead of 0

    def retrieve_products(self):
        response = requests.get('https://ecommerce-backend-api-dusky.vercel.app/api/products')

        data = response.json()
        return data["products"]

    def prompt_product_choice(self):
        product_index = input("Choose a product: ")

        # if EXIT we quit the program
        if (product_index.lower() == "exit" ):
            print("See ya later alligator")
            self.running = False
            return

        try:
            index = int(product_index)
            found_product = self.products[index]
            self.print_product_info(found_product)
        except:
            print("Invalid product index, try again")

    def print_product_info(self, product):
        print(f"\n\n--{product["name"]}------------")
        print(product["description"])
        print(f"Category: {product["category"]}")
        print(f"Price: ${product["price"]}")
        print(f"Stock: {product["stock"]} units\n\n")


app = EcommerceApp()