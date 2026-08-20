import time
import random
from technical_part import classes
from technical_part import statistics

products_in_grocery_store = ["chleb", "ryba", "jagody", "zupa", "bułka", "jabłko", "marchewka", "ziemniak"]
potions_in_magic_shop = ["mikstura regeneracji", "mikstura siły", "mikstura szybkości"]
player = statistics.player

def introduction_to_game():
    print(f"Witaj w zatoce wschodzącego słońca, to miejsce gdzie zawsze panuje lato, dobry nastrój oraz znajduje się piękny widok na wschód słońca")
    time.sleep(4)
    name = input("Wpisz imię dla swojej postaci: ")
    print(f"To tutaj zaczyna się twoja historia {name}! Zwiedzaj świat, nabieraj doświadczenia i zostaw swój ślad w historii tego miejsca!")
    time.sleep(4)

def random_unique_products(count, products):
    return random.sample(products, count)

def shopping_part():
    while True:
        print("==" * 50)
        print("Przechodzisz do handlowej części miasta, to tutaj znajdują się wszystkie sklepy!")
        time.sleep(3)
        shop_choice = input("""Do jakiego sklepu chcesz pójść? 
        a - spożywczy
        b - zbrojownia
        c - magiczny
        d - warsztat broni 
        e - powrót do głównej części miasta """)
        if shop_choice == "e":
            print("Opuszczasz handlową część miasta...")
            return
        elif shop_choice == "a":
            sklep_spożywczy = classes.Grocery_store("Sklep spożywczy")
            position1, position2, position3 = random_unique_products(3, products_in_grocery_store)
            sklep_spożywczy.shop_menu(position1, position2, position3, sklep_spożywczy.name)
        elif shop_choice == "b":
            zbrojownia = classes.Armor_store("Zbrojownia")
            zbrojownia.shop_menu("zbrojowni")
        elif shop_choice == "c":
            sklep_magiczny = classes.Magic_store("Magiczny sklep")
            position1, position2, position3 = random_unique_products(3, potions_in_magic_shop)
            sklep_magiczny.shop_menu(position1, position2, position3, sklep_magiczny.name)
        elif shop_choice == "d":
            sklep_z_bronia = classes.Weapon_store("Warsztat z bronią")
            sklep_z_bronia.shop_menu("warsztat z bronią")
        else:
            print("Nieprawidłowo wpisana komenda!")

def well(chance):
    print("==" * 50)
    decision = input("""Twoją uwagę przykuwa studnia stojąca w środku miejskiego placu, podchodzisz do niej...
Czy chcesz wrzucić monetę aby sprawdzić swoje szczęście? """)
    if decision == "tak" and player["monety"] >= 1:
        player["monety"] -= 1
        if chance <= 5:
            time.sleep(2)
            print("Dzisiaj szczęście jest po twojej stronie!")
            time.sleep(2)
            if chance <= 3:
                food_reward = random.randint(0, len(products_in_grocery_store) - 1)
                player["inventory"].append(products_in_grocery_store[food_reward])
                print(f"Udało ci się dostać {products_in_grocery_store[food_reward]}")
            else:
                potion_reward = random.randint(0, len(potions_in_magic_shop) - 1)
                player["inventory"].append(potions_in_magic_shop[potion_reward])
                print(f"Udało ci się dostać {potions_in_magic_shop[potion_reward]}")
        else:
            time.sleep(2)
            print("Dzisiaj szczęście nie jest po twojej stronie!")
    else:
        print("Odchodzisz od studni...")

def city():
    while True:
        print("==" * 50)
        inp = input("Witaj w Słonecznym mieście! Gdzie zmierzasz? a - sklepy, c - studnia, e - opuszczenie miasta ")
        if inp == "e":
            print("Opuszczasz miasto...")
            return
        elif inp == "a":
            shopping_part()
        elif inp == "b":
            pass
        elif inp == "c":
            well(random.randint(1, 10))
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