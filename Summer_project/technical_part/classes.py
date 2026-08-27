from technical_part.statistics import player

armor_types = ["miedziana zbroja", "złota zbroja", "żelazna zbroja", "diamentowa zbroja"]
sword_types = ["drewniany miecz", "żelazny miecz", "złoty miecz", "diamentowy miecz"]
axe_types = ["drewniana siekiera", "żelazna siekiera", "złota siekiera", "diamentowa siekiera"]

class Products_in_shops:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self, name):
        self.name = name

    def shop_menu(self, product1, product2, product3, place):
        available_products = [product1, product2, product3]
        print("==" * 50)
        options = input(f"Witaj w {place}, czy chcesz przejrzeć asortyment? ")
        if options == "tak":
            print(f"Dostępny asortyment: {product1}, {product2}, {product3}")
            inp = input("Czy chcesz coś kupić? ")
            if inp == "tak":
                product_to_buy = input("Co chcesz kupić? ")
                for i in available_products:
                    if product_to_buy == i:
                        print(f"Kupiłeś {product_to_buy}!")
                        player["inventory"].append(product_to_buy)
                        break
            else:
                print("Nie kupujesz nic.")
        else:
            print("Opuszczasz sklep...")

class Grocery_store(Shop):
    def __init__(self, name):
        super().__init__(name)

class Magic_store(Shop):
    def __init__(self, name):
        super().__init__(name)

class Armor_store:
    def __init__(self, name):
        self.name = name
    def armor_presentation(self):
        print("==" * 50)
        print("""Dostępna zbroja:
        Miedziana zbroja ---- 5 monet
        Złota zbroja ---- 15 monet
        Żelazna zbroja ---- 30 monet
        Diamentowa zbroja --- 50 monet
        """)
    def buying(self):
        armor_choice = input("Jaką zbroję chcesz kupić? ")
        if armor_choice in armor_types:
            armor_types.remove(armor_choice)
            player["zbroja"] = armor_choice
            print(f"Kupiłeś {armor_choice}!")
        else:
            print("Takiej zbroi nie ma w asortymencie sklepu!")

    def shop_menu(self, name):
        print("==" * 50)
        options = input(f"Witaj w {name}, tutaj możesz kupić różnego rodzaju zbroję! Czy chcesz przejrzeć asortyment? ")
        if options == "tak":
            self.armor_presentation()
            print("==" * 50)
            buy_or_not = input("Czy chcesz coś kupić? ")
            if buy_or_not == "tak":
                self.buying()
            else:
                print("Nie kupujesz nic.")
        else:
            print(f"Opuszczanie {name}...")

class Weapon_store:
    def __init__(self, name):
        self.name = name
    def weapon_presentation_SWORDS(self):
        print("==" * 50)
        print("""Dostępne miecze:
        Drewniany miecz ---- 5 monet
        Żelazny miecz ---- 15 monet
        Złoty miecz ---- 25 monet
        Diamentowy miecz --- 40 monet
        """)
    def weapon_presentation_AXES(self):
        print("==" * 50)
        print("""Dostępne siekiery:
        Drewniana siekiera ---- 10 monet
        Żelazna siekiera ---- 25 monet
        Złota siekiera ---- 40 monet
        Diamentowa siekiera --- 60 monet
        """)
    def buying_SWORDS(self):
        SWORD_choice = input("Jaki konkretnie miecz chcesz kupić? ")
        if SWORD_choice in sword_types:
            sword_types.remove(SWORD_choice)
            player["broń"] = SWORD_choice
            print(f"Kupiłeś {SWORD_choice}!")
        else:
            print("Takiej broni nie ma w asortymencie sklepu!")
    def buying_AXES(self):
        AXE_choice = input("Jaką konkretnie siekierę chcesz kupić? ")
        if AXE_choice in axe_types:
            axe_types.remove(AXE_choice)
            player["broń"] = AXE_choice
            print(f"Kupiłeś {AXE_choice}!")
        else:
            print("Takiej broni nie ma w asortymencie sklepu!")

    def shop_menu(self, name):
        print("==" * 50)
        options = input(f"""Witaj w {name}, tutaj możesz kupić różnego rodzaju broń! 
        Dostępna broń:
        -> miecze
        -> siekiery 
        Jaki typ broni chcesz przejrzeć? """)
        if options == "miecze":
            self.weapon_presentation_SWORDS()
        elif options == "siekiery":
            self.weapon_presentation_AXES()
        else:
            print(f"Opuszczanie {name}...")

        print("==" * 50)
        buy_or_not = input("Czy chcesz coś kupić? ")
        if buy_or_not == "tak":
            what_to_buy = input("Jaki typ broni chcesz kupić? ")
            if what_to_buy == "miecz":
                self.buying_SWORDS()
            elif what_to_buy == "siekiera":
                self.buying_AXES()
            else:
                print("Niepoprawnie wpisana komenda!")
        else:
            print("Nie kupujesz nic.")

#----------------------------------------------------------------------------------------------------

class Creature:
    def __init__(self, name, atk, hp, loot):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.loot = loot

#----------------------------------------------------------------------------------------------------

class Random_event:
    def __init__(self, name):
        self.name = name
    def random_event1(self, player, product, price):
        choice = input(f"""Udało ci się natknąć na błądzącego handlarza!
Proponuje ci ofertę: {product} za jedyne {price} monet!
Czy się zgadzasz na taką transakcję? tak/nie  """)
        if choice == "tak":
            player["inventory"].append(product)
            player["monety"] -= price
            print("Transakcja się powiodła! Idziesz dalej...")
        elif choice == "nie":
            print("Odchodzisz od handlarza i idziesz dalej...")
        else:
            print("Nieprawidłowa komenda!")

    #DODAĆ WIĘCEJ RANDOM EVENTÓW

#----------------------------------------------------------------------------------------------------

class Finding:
    def __init__(self,name):
        self.name = name
    def found(self, name):
        print(f"Udało ci się znalezć {name}")
        player["inventory"].append(name)
