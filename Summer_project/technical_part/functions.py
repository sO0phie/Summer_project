import time
import random

products_in_grocery_store = ["chleb", "ryba", "jagody", "zupa", "bułka", "jabłko", "marchewka", "ziemniak"]
final_products_in_grocery_store = []

def introduction_to_game():
    print(f"Witaj w zatoce wschodu słońca, to miejsce gdzie zawsze panuje lato, dobry nastrój oraz znajduje się piękny widok na wschód słońca")
    time.sleep(4)
    name = input("Wpisz imię dla swojej postaci: ")
    print(f"To tutaj zaczyna się twoja historia {name}! Zwiedzaj świat, nabieraj doświadczenia i zostaw swój ślad w historii tego miejsca!")
    time.sleep(4)

class Products_in_shops:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self, name):
        self.name = name

    def shop_menu(self, product1, product2, product3, place):
        available_products = [product1, product2, product3]
        options = input(f"Witaj w {place}, czy chcesz przejrzeć asortyment? ")
        if options == "tak":
            print(f"Dostępny asortyment: {product1}, {product2}, {product3}")
            inp = input("Czy chcesz coś kupić? ")
            if inp == "tak":
                product_to_buy = input("Co chcesz kupić? ")
                verification = [p for p in available_products]
                if product_to_buy in verification:
                    print(f"Kupiłeś {product_to_buy}!")
                else:
                    print("Nie ma takiego produktu w sklepie!")
            else:
                print("Nie kupujesz nic.")
        else:
            print("Opuszczasz sklep...")

class Grocery_store(Shop):
    def __init__(self, name):
        super().__init__(name)

def random_unique_products(count, products):
    return random.sample(products, count)

def city():
    while True:
        print("==" * 50)
        inp = input("Witaj w Słonecznym mieście! Gdzie zmierzasz? a - sklep, e - opuszczenie miasta ")
        if inp == "a":
            sklep_spożywczy = Grocery_store("Sklep spożywczy")
            position1, position2, position3 = random_unique_products(3, products_in_grocery_store)
            sklep_spożywczy.shop_menu(position1, position2, position3, sklep_spożywczy.name)
        elif inp == "e":
            print("Opuszczasz miasto...")
            return
        else:
            print("Niepoprawnie wskazany kierunek!")

def direction(choice: str):
    if choice == "a":
        print("Idziesz do miasta")
        time.sleep(2)
        city()
    elif choice == "b":
        print("Idziesz nad morze")
    else:
        print("Niepoprawnie wskazany kierunek!")