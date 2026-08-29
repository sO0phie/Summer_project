import time
import random
from technical_part import classes
from technical_part import statistics

products_in_grocery_store = ["chleb", "ryba", "jagody", "zupa", "bułka", "jabłko", "marchewka", "ziemniak"]
potions_in_magic_shop = ["mikstura regeneracji", "mikstura siły", "mikstura szybkości"]
found_things = ["muszelka", "patyk", "skorupka"]
unfriendly_sea_animals = ["Krab", "Krewetka", "Drapieżny ptak"]
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
            sklep_spożywczy.shop_menu(position1, position2, position3, sklep_spożywczy.name, random.randint(2, 7))
        elif shop_choice == "b":
            zbrojownia = classes.Armor_store("Zbrojownia")
            zbrojownia.shop_menu("zbrojowni")
        elif shop_choice == "c":
            sklep_magiczny = classes.Magic_store("Magiczny sklep")
            position1, position2, position3 = random_unique_products(3, potions_in_magic_shop)
            sklep_magiczny.shop_menu(position1, position2, position3, sklep_magiczny.name, random.randint(5, 10))
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

#---------------------------------------------------------------------------------------------------------------------------

def fighting(opponent, player ,chance) -> bool:
    while player["hp"] > 0 and opponent.hp > 0:
        fight_or_run = input(f"""{opponent.name} chce Cię atakować!
        a - walka, b - próba ucieczki """)
        if fight_or_run == "a":
            print(f"Atakujesz {opponent.name}!")
            opponent.hp -= player['atk']
            print(f"Hp {opponent.name}: {opponent.hp}")
            time.sleep(1)
            if opponent.hp <= 0:
                print(f"Udało Ci się pokonać {opponent.name}! Dostajesz {opponent.loot}")
                player["inventory"].append(opponent.loot)
                print("==="*50)
                return True
            print(f"{opponent.name} cię atakuje!")
            if opponent.atk > player.get("defense", 0):
                damage_taken = opponent.atk - player.get("defense", 0)
            else:
                damage_taken = 0
            player['hp'] -= damage_taken
            print(f"Otrzymujesz {damage_taken} obrażeń. Twoje hp: {player['hp']}")
            time.sleep(1)
            if player["hp"] <= 0:
                return False
        elif fight_or_run == "b":
            if chance <= 2:
                print("Udało ci się uciec!")
                print("==="*50)
                return True
            else:
                print(f"Nie udało ci się uciec, w międzyczasie {opponent.name} zadaje ci obrażenie!")
                time.sleep(2)
                if opponent.atk > player.get("defense", 0):
                    damage_taken = opponent.atk - player.get("defense", 0)
                else:
                    damage_taken = 0
                player["hp"] -= damage_taken
                print(f"Otrzymujesz {damage_taken} obrażeń. Twoje hp: {player['hp']}")
                if player["hp"] <= 0:
                    return False
        else:
            print("Niepoprawnie wpisana komenda!")
    print("==="*50)
    return False

#---------------------------------------------------------------------------------------------------------------------------
def finding_something(chance_of_finding):
    time.sleep(2)
    print("==="*50)
    if chance_of_finding <= 5:
        znalezione = classes.Finding("znalezione")
        znalezione.found(found_things[random.randint(0, len(found_things) - 1)])
    elif chance_of_finding == 6:
        atk_przeciw = random.randint(1, 3)
        hp_przeciw = random.randint(2, 5)
        loot_przeciw = found_things[random.randint(0, len(found_things) - 1)]
        przeciwnik = classes.Creature(unfriendly_sea_animals[random.randint(0, len(unfriendly_sea_animals) - 1)], atk_przeciw, hp_przeciw, loot_przeciw)
        return fighting(przeciwnik, player, random.randint(1, 5))
    elif chance_of_finding == 7 or chance_of_finding == 8:
        random_event = classes.Random_event("event")
        a = random.randint(1, 3)
        if a == 1:
            offer = products_in_grocery_store + potions_in_magic_shop
            random_event.random_event1(player, offer[random.randint(0, len(offer) - 1)], random.randint(3, 10))
        elif a == 2:
            sand_result = random_event.random_event2(random.randint(1, 3), random.randint(5, 10), player)
            if sand_result == False:
                print("Piasek zaczyna się sam osuwać, to nie wróży nic dobrego!")
                time.sleep(2)
                atk_przeciw = random.randint(1, 3)
                hp_przeciw = random.randint(2, 5)
                loot_przeciw = found_things[random.randint(0, len(found_things) - 1)]
                przeciwnik = classes.Creature(unfriendly_sea_animals[random.randint(0, len(unfriendly_sea_animals) - 1)], atk_przeciw, hp_przeciw, loot_przeciw)
                return fighting(przeciwnik, player, random.randint(1, 5))
        else:
            random_event.random_event3(player, random.randint(1, 3))
    else:
        print('eeeee')

        #DODAĆ JESZCZE OPCJĘ ZE ZNALEZIENIEM BOSSA LUB PORTALU DO INNEJ RZECZYWISTOŚCI

def sea():
    time.sleep(2)
    print("==="*50)
    print("Po jakimś czasie udało ci się dotrzeć do plaży...")
    while True:
        choice = input("a - iść dalej, e - powrót do rozdroża ")
        if choice == "e":
            break
        elif choice == "a":
            print("Decydujesz się iść dalej...")
            if finding_something(random.randint(1, 10)) is False:
                return False
        else:
            print("Niepoprawnie wpisana komenda!")

def direction(choice: str):
    if choice == "a":
        print("Idziesz do miasta")
        time.sleep(2)
        city()
    elif choice == "b":
        print("Idziesz nad morze")
        return sea()
    else:
        print("Niepoprawnie wskazany kierunek!")