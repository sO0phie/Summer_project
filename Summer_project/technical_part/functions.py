import time
import random
from technical_part import classes
from technical_part import statistics
from worlds.underwater import under_the_water

products_in_grocery_store = ["chleb", "ryba", "jagody", "zupa", "bułka", "jabłko", "marchewka", "ziemniak"]
potions_in_magic_shop = ["mikstura regeneracji", "mikstura siły", "mikstura szybkości"]
found_things = ["muszelka", "patyk", "skorupka"]
unfriendly_sea_animals = ["Krab", "Krewetka", "Drapieżny ptak"]
valuable_award = ["złota moneta", "srebrna moneta", "diament", "rubin", "szafir"]
underwater_treasure = ["złota moneta", "srebrna moneta", "diament", "rubin", "szafir", "mikstura regeneracji", "mikstura siły", "mikstura szybkości"]
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
        f - rynek  
        g - tawerna
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
        elif shop_choice == "f":
            sellable_list = underwater_treasure + valuable_award + found_things
            rynek = classes.Market("Rynek")
            rynek.sell(player, sellable_list, random.randint(5, 30))
        elif shop_choice == "g":
            tawerna = classes.Tavern("Tawerna")
            tawerna.tavern_menu()
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

def usable_items(player) -> list:
    usable_items_in_player_inventory = []
    all_usable_items = products_in_grocery_store + potions_in_magic_shop
    for item in player["inventory"]:
        if item in all_usable_items:
            usable_items_in_player_inventory.append(item)
    return usable_items_in_player_inventory

def usage_of_useful_items(player, list_of_usable_items) -> bool:
    if len(list_of_usable_items) == 0:
        print("Nie masz żadnych przedmiotów, które możesz użyć!")
        return False
    else:
        print("Masz następujące przedmioty w swoim ekwipunku które możesz użyć: ")
        for item in list_of_usable_items:
            print(item)
        inp = input("Czy chcesz użyć jakiegoś przedmiotu? ")
        if inp == "tak":
            inp = input("Jaki przedmiot chcesz użyć? ")
            if inp in list_of_usable_items:
                if inp in products_in_grocery_store:
                    print(f"Używasz {inp} i odzyskujesz 5 hp!")
                    player["hp"] += 5
                    player["inventory"].remove(inp)
                elif inp in potions_in_magic_shop:
                    if inp == "mikstura regeneracji":
                        print(f"Używasz {inp} i odzyskujesz 10 hp!")
                        player["hp"] += 10
                        player["inventory"].remove(inp)
                    elif inp == "mikstura siły":
                        print(f"Używasz {inp} i zwiększasz swoją siłę o 2!")
                        player["atk"] += 2
                        player["inventory"].remove(inp)
                    elif inp == "mikstura szybkości":
                        print(f"Używasz {inp} i zwiększasz swoją obronę o 2!")
                        player["defense"] += 2
                        player["inventory"].remove(inp)
            else:
                print("Nie masz takiego przedmiotu w swoim ekwipunku!")
                return False
        elif inp == "nie":
            return False
        else:
            print("Niepoprawnie wpisana komenda!")
            return False
    return True
#---------------------------------------------------------------------------------------------------------------------------

def fighting(opponent, player, chance, if_boss) -> bool:
    while player["hp"] > 0 and opponent.hp > 0:
        chance_of_super_attack = random.randint(1, 10)
        fight_or_run = input(f"""{opponent.name} chce Cię atakować!
        a - walka, b - próba ucieczki, u - użyj przedmiotu z ekwipunku """)
        if fight_or_run == "u":
            usage_of_useful_items(player, usable_items(player))
        elif fight_or_run == "a":
            print(f"Atakujesz {opponent.name}!")
            opponent.hp -= player['atk']
            print(f"Hp {opponent.name}: {opponent.hp}")
            time.sleep(1)
            if opponent.hp <= 0:
                if if_boss == True:
                    print(f"Udało Ci się pokonać {opponent.name}! Dostajesz {opponent.loot} oraz specjalny przedmiot {opponent.unique_award}!")
                    player["inventory"].append(opponent.unique_award)
                else:
                    print(f"Udało Ci się pokonać {opponent.name}! Dostajesz {opponent.loot}")
                player["inventory"].append(opponent.loot)
                print("==="*50)
                return True
            print(f"{opponent.name} cię atakuje!")
            if if_boss == True and chance_of_super_attack <= 3:
                print(f"{opponent.name} wykonuje super atak!")
                time.sleep(1)
                attack_damage = opponent.atk * 2
                if attack_damage > player.get("defense"):
                    damage_taken = attack_damage - player.get("defense")
                else:
                    damage_taken = 0
            else:
                if opponent.atk > player.get("defense"):
                    damage_taken = opponent.atk - player.get("defense")
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
                if if_boss == True and chance_of_super_attack <= 3:
                    print(f"{opponent.name} wykonuje super atak!")
                    time.sleep(1)
                    attack_damage = opponent.atk * 2
                    if attack_damage > player.get("defense"):
                        damage_taken = attack_damage - player.get("defense")
                    else:
                        damage_taken = 0
                else:
                    if opponent.atk > player.get("defense"):
                        damage_taken = opponent.atk - player.get("defense")
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

def activating_the_portal(key_to_portal, player_inventory) -> bool:
    decision = input("Czy chcesz aktywować portal? ")
    if decision == "tak":
        if key_to_portal in player_inventory:
            print("Aktywujesz portal")
            print("=="*50)
            return True
        else:
            print("Nie masz klucza aby aktywować portal, wróć kiedy go zdobędziesz!")
            return False
    else:
        print("Odchodzisz od portalu...")
    return False
        
def discovering_portal() -> bool:
    if player.get("portal_found") == True:
        return False
    print(".....")
    time.sleep(2)
    print("Po długiej wędrówce w końcu udaję ci się znalezć portal do innego świata!")
    time.sleep(3)
    print("Decydujesz się podejść bliżej...")
    player["portal_found"] = True
    return True

#---------------------------------------------------------------------------------------------------------------------------

def finding_something(chance_of_finding):
    time.sleep(2)
    print("==="*50)
    if chance_of_finding <= 5:
        znalezione = classes.Finding("znalezione")
        znalezione.found(found_things[random.randint(0, len(found_things) - 1)])
        return True
    elif chance_of_finding == 6:
        atk_przeciw = random.randint(1, 3)
        hp_przeciw = random.randint(2, 5)
        loot_przeciw = found_things[random.randint(0, len(found_things) - 1)]
        award = random.randint(2, 6)
        przeciwnik = classes.Creature(unfriendly_sea_animals[random.randint(0, len(unfriendly_sea_animals) - 1)], atk_przeciw, hp_przeciw, loot_przeciw, award)
        return fighting(przeciwnik, player, random.randint(1, 5), if_boss = False)
    elif chance_of_finding == 7 or chance_of_finding == 8:
        random_event = classes.Random_event("event")
        a = random.randint(1, 3)
        if a == 1:
            offer = products_in_grocery_store + potions_in_magic_shop
            random_event.random_event1(player, offer[random.randint(0, len(offer) - 1)], random.randint(3, 10))
            return True
        elif a == 2:
            sand_result = random_event.random_event2(random.randint(1, 3), random.randint(5, 10), player)
            if sand_result is True:
                return True
            if sand_result is False:
                print("Piasek zaczyna się sam osuwać, to nie wróży nic dobrego!")
                time.sleep(2)
                atk_przeciw = random.randint(1, 3)
                hp_przeciw = random.randint(2, 5)
                award = random.randint(2, 6)
                loot_przeciw = found_things[random.randint(0, len(found_things) - 1)]
                przeciwnik = classes.Creature(unfriendly_sea_animals[random.randint(0, len(unfriendly_sea_animals) - 1)], atk_przeciw, hp_przeciw, loot_przeciw, award)
                return fighting(przeciwnik, player, random.randint(1, 5), if_boss = False)
            return True
        else:
            random_event.random_event3(player, random.randint(1, 3))
            return True
    elif chance_of_finding == 9:
        atk_scorp = random.randint(3, 5)
        hp_scorp = random.randint(10, 15)
        big_award = random.randint(10, 20)
        loot_boss = valuable_award[random.randint(0, len(valuable_award) - 1)]
        scorpion = classes.Boss("Skorpion", atk_scorp, hp_scorp, loot_boss, big_award, "klucz do portalu")
        scorpion.boss_fight()
        return fighting(scorpion, player, random.randint(1, 6), if_boss = True)
    else:
        discovering_portal()
        activating_the_portal("klucz do portalu", player["inventory"])
        return True

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
    elif choice == "c":
        print("Idziesz do portalu...")
        time.sleep(3)
        if activating_the_portal("klucz do portalu", player["inventory"]) is True:
            print("Przechodzisz przez portal")
            return under_the_water(player)
        else:
            return True
    else:
        print("Niepoprawnie wskazany kierunek!")

#---------------------------------------------------------------------------------------------------------------------------
def sunk_ship(chance):
    print("==="*50)
    inp = input("Znajdujesz zatonięty statek, czy chcesz go eksplorować? ")
    time.sleep(2)
    if inp == "tak":
        print("Wpływasz do wnętrza statku...")
        print("....")
        time.sleep(3)
        if chance == 1:
            print("Korpus statka zaczyna się rozpadać, musisz uciekać! ")
            time.sleep(2)
            if random.randint(1, 5) <= 2:
                print("Udało ci się uciec z zatopionego statku!")
            else:
                print("Nie udało ci się uciec, ale po krótkim czasie udaje ci się wydostać spod desek statku, niestety tracisz 10 hp!")
                player["hp"] -= 10
        elif chance == 2:
            print("W środku statku znajdujesz skrzynię pełną złota!")
            treasure = classes.Finding("znalezione")
            treasure.found("skrzynia ze złotem")
            player["inventory"].append(treasure.name)
        else:
            print("Statek okazał się być pusty, wypływasz i kontynuujesz swoją podróż...")
    else:
        print("Odpływasz od zatoniętego statku i kontynuujesz swoją podróż...")

def buried_treasure(chance) -> bool:
    print("==="*50)
    inp = input("Znajdujesz zakopany skarb, czy chcesz go odkopać? ")
    if inp == "tak":
        time.sleep(3)
        print("Odkopujesz skarb...")
        time.sleep(2)
        print("....")
        if chance <= 3:
            treasure = classes.Finding("znalezione")
            treasure.found(underwater_treasure[random.randint(0, len(underwater_treasure) - 1)])
            print(f"Odkopujesz skarb i znajdujesz {treasure.name}!")
            return True
        elif chance > 3 and chance <= 6:
            litter = classes.Finding("znalezione")
            litter.found(found_things[random.randint(0, len(found_things) - 1)])
            print(f"Odkopujesz skarb i znajdujesz {litter.name}. Może następnym razem uda ci się znalezć coś lepszego!")
            player["inventory"].append(litter.name)
            return True
        elif chance > 6 and chance <= 8:
            print("Odkopujesz skarb, ale nie znajdujesz tam nic...")
            time.sleep(2)
            print("Odwracasz się, chcesz już odejść, ale.....")
            time.sleep(3)
            return fighting(classes.Creature(unfriendly_sea_animals[random.randint(0, len(unfriendly_sea_animals) - 1)], random.randint(1, 3), random.randint(2, 5), found_things[random.randint(0, len(found_things) - 1)], random.randint(2, 6)), player, random.randint(1, 5), if_boss = False)
        else:
            print("Nie udało ci się znaleźć niczego wartościowego, ale przynajmniej nie straciłeś czasu!")
            return True
    else:
        print("Decydujesz się nie odkopywać skarbu i kontynuujesz swoją podróż...")
        return True

def underwater_choice() -> bool:
    print("==="*50)
    while True:
        print("==="*50)
        choice = input("a - płynąć dalej, e - powrót do początkowego miejsca  ")
        if choice == "e":
            print("Wracasz do menu głównego podwodnego świata...")
            return True
        elif choice == "a":
            print("Decydujesz się płynąć głębiej...")
            chance = random.randint(1, 12)
            if chance == 1 or chance == 10:
                print("Znalazłeś coś ciekawego!")
                time.sleep(2)
                znalezione = classes.Finding("znalezione")
                znalezione.found(underwater_treasure[random.randint(0, len(underwater_treasure) - 1)])
            elif chance > 1 and chance <= 6:
                atk_przeciw = random.randint(1, 3)
                hp_przeciw = random.randint(2, 5)
                award = random.randint(2, 6)
                loot_przeciw = found_things[random.randint(0, len(found_things) - 1)]

                if chance == 2 or chance == 3:
                    time.sleep(2)
                    calamar = classes.Calamar("Kałamarnica", atk_przeciw, hp_przeciw, loot_przeciw, award)
                    result = fighting(calamar, player, random.randint(1, 5), if_boss = False)
                    if result is False:
                        return False
                elif chance == 4:
                    time.sleep(2)
                    piranha = classes.Piranha("Piranha", atk_przeciw, hp_przeciw, loot_przeciw, award)
                    result = fighting(piranha, player, random.randint(1, 5), if_boss = False)
                    if result is False:
                        return False
                elif chance == 5:
                    time.sleep(2)
                    fugu = classes.Fugu("Fugu", atk_przeciw, hp_przeciw, loot_przeciw, award)
                    result = fighting(fugu, player, random.randint(1, 5), if_boss = False)
                    if result is False:
                        return False
                elif chance == 6:
                    time.sleep(2)
                    atk_przeciw = random.randint(5, 10)
                    hp_przeciw = random.randint(7, 12)
                    award = random.randint(5, 14)
                    loot_przeciw = underwater_treasure[random.randint(0, len(underwater_treasure) - 1)]
                    shark = classes.Shark("Rekin", atk_przeciw, hp_przeciw, loot_przeciw, award)
                    result = fighting(shark, player, random.randint(1, 5), if_boss = False)
                    if result is False:
                        return False
            elif chance == 7:
                result = sunk_ship(random.randint(1,3))
                if result is False:
                    return False
            elif chance == 8:
                result = buried_treasure(random.randint(1, 10))
                if result is False:
                    return False
            elif chance == 9:
                atk_levi = random.randint(8, 14)
                hp_levi = random.randint(20, 30)
                big_award = random.randint(20, 40)
                loot_boss = valuable_award[random.randint(0, len(valuable_award) - 1)]
                leviathan = classes.Boss("Leviathan", atk_levi, hp_levi, loot_boss, big_award, "trójząb")
                leviathan.boss_fight()
                return fighting(leviathan, player, random.randint(1, 6), if_boss = True)
            else:
                print("Nie znajdujesz nic ciekawego, więc płyniesz dalej...")
        else:
            print("Niepoprawnie wpisana komenda!")
