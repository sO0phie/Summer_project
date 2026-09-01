from technical_part.statistics import player
import time
import random

armor_types = ["miedziana zbroja", "złota zbroja", "żelazna zbroja", "diamentowa zbroja"]
sword_types = ["drewniany miecz", "żelazny miecz", "złoty miecz", "diamentowy miecz"]
axe_types = ["drewniana siekiera", "żelazna siekiera", "złota siekiera", "diamentowa siekiera"]
ducks = ["mała kaczka", "duża kaczka", "kaczka z długim dziobem", "kaczka z długimi skrzydłami"]

class Products_in_shops:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Market:
    def __init__(self, name):
        self.name = name
    def sell(self, player, sellable_items, price):
        print("==" * 50)
        print(f"Witaj na rynku, tutaj możesz sprzedać swoje przedmioty i zyskać monety!")
        inp = input("Czy chcesz sprzedać coś ze swojego ekwipunku? ")
        if inp == "tak":
            if len(player["inventory"]) > 0:
                for item in player["inventory"]:
                    print(item)
                item_to_sell = input("Co chcesz sprzedać? ")
                if item_to_sell in sellable_items:
                    if item_to_sell in player["inventory"]:
                        player["inventory"].remove(item_to_sell)
                        player["monety"] += price
                        print(f"Sprzedajesz {item_to_sell} za {price} monet!")
                    else:
                        print("Nie masz takiego przedmiotu w swoim ekwipunku!")
                else:
                    print("Taki przedmiot nie jest dostępny do sprzedaży!")
            else:
                print("Wygląda na to że nie masz nic w swoim ekwipunku do sprzedania!")
        elif inp == "nie":
            print("Nie sprzedajesz niczego i opuszczasz rynek...")
        else:
            print("Niepoprawnie wpisana komenda! Opuszczasz rynek...")

class Shop:
    def __init__(self, name):
        self.name = name

    def shop_menu(self, product1, product2, product3, place, price):
        available_products = [product1, product2, product3]
        print("==" * 50)
        options = input(f"Witaj w {place}, czy chcesz przejrzeć asortyment? ")
        if options == "tak":
            print(f"Dostępny asortyment: {product1}, {product2}, {product3}")
            inp = input("Czy chcesz coś kupić? ")
            if inp == "tak":
                product_to_buy = input("Co chcesz kupić? ")
                if product_to_buy in available_products:
                    inp = input(f"{product_to_buy} kosztuje {price}, czy chcesz go kupić? ")
                    if inp == "tak":
                        if player["monety"] >= price:
                            print(f"Kupiłeś {product_to_buy}!")
                            player["inventory"].append(product_to_buy)
                            player["monety"] -= price
                        else:
                            print(f"Nie masz wystarczająco monet, aby kupić {product_to_buy}!")
                    else:
                        print("Nie kupujesz nic.")
                else:
                    print("Takiego produktu nie ma w asortymencie.")
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
        print("Dostępna zbroja:")
        prices = {
            "miedziana zbroja": 5,
            "złota zbroja": 15,
            "żelazna zbroja": 30,
            "diamentowa zbroja": 50,
        }
        if len(armor_types) > 0:
            for armor in armor_types:
                print(f"{armor} ---- {prices[armor]} monet")
        else:
            print("Brak dostępnych zbroi w sklepie.")
    def buying(self):
        armor_choice = input("Jaką zbroję chcesz kupić? ")
        if armor_choice in armor_types:
            price = 0
            defense = 0 
            if armor_choice == "miedziana zbroja":
                price = 5
                defense = 4
            elif armor_choice == "złota zbroja":
                price = 15
                defense = 7
            elif armor_choice == "żelazna zbroja":
                price = 30
                defense = 10
            elif armor_choice == "diamentowa zbroja":
                price = 50
                defense = 15

            if player["monety"] >= price:
                previous_armor = player.get("zbroja")
                if previous_armor == "miedziana zbroja":
                    player["defense"] -= 4
                elif previous_armor == "złota zbroja":
                    player["defense"] -= 7
                elif previous_armor == "żelazna zbroja":
                    player["defense"] -= 10
                elif previous_armor == "diamentowa zbroja":
                    player["defense"] -= 15
                player["monety"] -= price
                if armor_choice in armor_types:
                    armor_types.remove(armor_choice)
                player["zbroja"] = armor_choice
                player["defense"] += defense
                print(f"Kupiłeś {armor_choice}! Twoja obrona wzrosła o {defense}.")
            else:
                print("Nie masz wystarczająco monet aby kupić tą zbroję!")
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
        print("Dostępne miecze:")
        prices = {
            "drewniany miecz": 5,
            "żelazny miecz": 15,
            "złoty miecz": 25,
            "diamentowy miecz": 40,
        }
        if sword_types:
            for sword in sword_types:
                print(f"{sword} ---- {prices[sword]} monet")
        else:
            print("Brak dostępnych mieczy w sklepie.")
    def weapon_presentation_AXES(self):
        print("==" * 50)
        print("Dostępne siekiery:")
        prices = {
            "drewniana siekiera": 10,
            "żelazna siekiera": 25,
            "złota siekiera": 40,
            "diamentowa siekiera": 60,
        }
        if axe_types:
            for axe in axe_types:
                print(f"{axe} ---- {prices[axe]} monet")
        else:
            print("Brak dostępnych siekier w sklepie.")
    def buying_SWORDS(self):
        SWORD_choice = input("Jaki konkretnie miecz chcesz kupić? ")
        if SWORD_choice in sword_types:
            prices = {
                "drewniany miecz": 5,
                "żelazny miecz": 15,
                "złoty miecz": 25,
                "diamentowy miecz": 40,
            }
            sword_atk = {
                "drewniany miecz": 2,
                "żelazny miecz": 5,
                "złoty miecz": 8,
                "diamentowy miecz": 12,
            }
            price = prices.get(SWORD_choice)
            if player["monety"] >= price:
                previous_weapon = player.get("broń")
                if previous_weapon in sword_atk:
                    player["atk"] -= sword_atk[previous_weapon]
                player["monety"] -= price
                if SWORD_choice in sword_types:
                    sword_types.remove(SWORD_choice)
                player["broń"] = SWORD_choice
                player["atk"] += sword_atk.get(SWORD_choice)
                print(f"Kupiłeś {SWORD_choice}! Twoje atk wzrosło o {sword_atk.get(SWORD_choice)}.")
            else:
                print("Nie masz wystarczająco monet aby kupić ten miecz!")
        else:
            print("Takiej broni nie ma w asortymencie sklepu!")
    def buying_AXES(self):
        AXE_choice = input("Jaką konkretnie siekierę chcesz kupić? ")
        if AXE_choice in axe_types:
            prices = {
                "drewniana siekiera": 10,
                "żelazna siekiera": 25,
                "złota siekiera": 40,
                "diamentowa siekiera": 60,
            }
            axe_atk = {
                "drewniana siekiera": 3,
                "żelazna siekiera": 6,
                "złota siekiera": 10,
                "diamentowa siekiera": 15,
            }
            price = prices.get(AXE_choice)
            if player["monety"] >= price:
                previous_weapon = player.get("broń")
                if previous_weapon in axe_atk:
                    player["atk"] -= axe_atk[previous_weapon]
                player["monety"] -= price
                if AXE_choice in axe_types:
                    axe_types.remove(AXE_choice)
                player["broń"] = AXE_choice
                player["atk"] += axe_atk.get(AXE_choice)
                print(f"Kupiłeś {AXE_choice}! Twoje atk wzrosło o {axe_atk.get(AXE_choice)}.")
            else:
                print("Nie masz wystarczająco monet aby kupić tę siekierę!")
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

def duck_race():
    print("Witaj w wyścigu kaczek! Tutaj możesz obstawiać swoje monety na jedną z czterech dostępnych kaczek!")
    time.sleep(2)
    print("Dostępne kaczki:")
    for duck in ducks:
        print(duck)
        time.sleep(1)
    bet = input("Na którą kaczkę chcesz postawić swoje monety? ")
    if bet in ducks:
        amount_bet = int(input("Ile monet chcesz postawić? "))
        if amount_bet <= player["monety"]:
            print(f'Postawiłeś {amount_bet} monet na kaczkę {bet}!')
            time.sleep(2)
            print("Rozpoczynamy wyścig...")
            time.sleep(3)
            winning_duck = ducks[random.randint(0, 3)]
            while True:
                print("..."*20)
                time.sleep(1)
                print("Kaczki biegną...")
                time.sleep(2)
                leader_duck = ducks[random.randint(0, 3)]
                print(f"Narazie na prowadzeniu jest {leader_duck}!")
                time.sleep(2)
                if random.randint(1, 3) == 3:
                    print(f"{winning_duck} przekracza metę i wygrywa!")
                    if winning_duck == bet:
                        winning= int(amount_bet) * 2
                        player["monety"] += winning
                        print(f"Gratulacje! Twoja kaczka wygrała! Zdobywasz {winning} monet!")
                    else:
                        print(f'Wygrywa {winning_duck}!')
                        player["monety"] -= int(amount_bet)
                        print(f"Niestety twoja kaczka przegrała! Przegrywasz {amount_bet} monet!")
                    break
        else:
            print("Nie masz wystarczająco monet aby postawić taką kwotę!")
    else:
        print("Niepoprawnie wpisana komenda! Opuszczasz wyścig kaczek...")

#----------------------------------------------------------------------------------------------------

class Tavern:
    def __init__(self, name):
        self.name = name
    def tavern_menu(self):
        print("==" * 50)
        print(f"Witaj w tawernie 'Pod gwiazdami', tutaj możesz odpocząć i zregenerować swoje zdrowie, bądz spotkać innych podróżników!")
        inp = input("""Co chcesz zrobić?
        a - odpocząć w tawernie (koszt 10 monet, regeneruje 10 hp)
        b - wejść w głąb tawerny
        e - wyjść z tawerny """)
        if inp == "a":
            if player["monety"] >= 10:
                player["monety"] -= 10
                player["hp"] += 10
                print("Odpoczywasz...")
                time.sleep(4)
                print("Odpoczywasz w tawernie i regenerujesz swoje zdrowie o 10 hp!")
                time.sleep(2)
                print("Opuszczasz tawernę i idziesz dalej...")
            else:
                print("Nie masz wystarczająco monet aby odpocząć w tawernie!")
        elif inp == "b":
            print("Wchodzisz w głąb tawerny...")
            time.sleep(3)
            print("=="*50)
            print("Twoją uwagę przykuwa grupa podróżników stojących dookoła stołu, skąd dobiegają odgłosy kaczek, decydujesz się podejść bliżej...")
            time.sleep(3)
            duck_race()
        elif inp == "e":
            print("Opuszczasz tawernę...")
        else:
            print("Niepoprawnie wpisana komenda! Opuszczasz tawernę...")

#----------------------------------------------------------------------------------------------------

class Creature:
    def __init__(self, name, atk, hp, loot, money):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.loot = loot
        self.money = money

class Boss(Creature):
    def __init__(self, name, atk, hp, loot, money, unique_award):
        super().__init__(name, atk, hp, loot, money)
        self.unique_award = unique_award
    def boss_fight(self):
        print("Idziesz przed siebie...")
        time.sleep(2)
        print(f"Nagle spod piasku wyskakuje na ciebie grozny {self.name}! Szykuj sie do walki!")

class Calamar(Creature):
    def __init__(self, name, atk, hp, loot, money):
        super().__init__(name, atk, hp, loot, money)
    def calamar_fight(self):
        print("Płyniesz...")
        time.sleep(3)
        print(f"Nagle podpływa do ciebie mała agresywna kałamarnica! Szykuj sie do walki!")

class Piranha(Creature):
    def __init__(self, name, atk, hp, loot, money):
        super().__init__(name, atk, hp, loot, money)
    def piranha_fight(self):
        print("Płyniesz...")
        time.sleep(3)
        print(f"Nagle podpływa do ciebie agresywna pirania! Szykuj sie do walki!")

class Fugu(Creature):
    def __init__(self, name, atk, hp, loot, money):
        super().__init__(name, atk, hp, loot, money)
    def fugu_fight(self):
        print("Płyniesz...")
        time.sleep(3)
        print(f"Nie zauważasz niczego, ale nagle czujesz jak coś cię uderza w bok! To agresywna ryba fugu! Szykuj sie do walki!")

class Shark(Creature):
    def __init__(self, name, atk, hp, loot, money):
        super().__init__(name, atk, hp, loot, money)
    def shark_fight(self):
        print("Płyniesz...")
        time.sleep(3)
        print(f"Nagle podpływa do ciebie ogromny rekin! Szykuj sie do walki!")

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
            print("==="*50)
            return True
        elif choice == "nie":
            print("Odchodzisz od handlarza i idziesz dalej...")
            print("==="*50)
            return False
        else:
            print("Nieprawidłowa komenda!")
            print("==="*50)
            return False

    def random_event2(self, chance, amount_of_coins, player):
        inp = input("Napotykasz na małą górke z piaskiem. Czy chcesz ją odkopać? ")
        print("==="*50)
        if inp == "tak":
            if chance == 2:
                print(".....")
                time.sleep(2)
                print(f"Udało ci się znalezć skrzynię z monetami! Zdobywasz {amount_of_coins} monet!")
                player["monety"] += amount_of_coins
                return True
            print("Nie znajduje nic wartościowego, więc odchodzisz od góry piasku.")
            return False
        elif inp == "nie":
            print("Omijasz górke i idziesz dalej")
            return None
        else:
            print("Nieprawidłowa komenda! Omijasz górkę i idziesz dalej.")
            return None

    def random_event3(self, player, random):
        time.sleep(3)
        inp = input("""Po długim błądzeniu spotykasz na swojej drodze błyszczącą cząstkę
Czy chcesz ją zbadać? tak/nie """)
        if inp == "tak":
            print("Podchodzisz bliżej i dotykasz świecącą sie cząstkę...")
            time.sleep(2)
            if random == 1:
                player["atk"] += 5
                print("Czujesz się inaczej, po chwili czujesz jak twoja siła się zwiększa! Zdobywasz 5 atk!")
            elif random == 2:
                player["hp"] += 5
                print("Czujesz się inaczej, po chwili czujesz jak twoje ciało się regeneruje! Zdobywasz 5 hp!")
            elif random == 3:
                player["monety"] += 10
                print("Zdobywasz 10 monet!")
            print("==="*50)
            return True
        else:
            print("Odchodzisz od cząstki i idziesz dalej...")
            print("==="*50)
            return False

#----------------------------------------------------------------------------------------------------

class Finding:
    def __init__(self,name):
        self.name = name
    def found(self, name):
        print(f"Udało ci się znalezć {name}")
        player["inventory"].append(name)
