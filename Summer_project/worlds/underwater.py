import time
from technical_part import functions
from technical_part.statistics import player

def under_the_water(player) -> bool:
    print("Witaj w podwodnym świecie! Jest to miejsce pełne tajemnic i niebezpieczeństw. Musisz być ostrożny, aby przetrwać w tym środowisku!")
    while player["hp"] > 0 and player["hp"] != 0:
        print("=="*50)
        inp = input("Co chcesz zrobić? a - eksploracja głębin, b - sprawdzenie statystyk, c - powrót na powierzchnię ")
        if inp == "a":
            print("Zanurzasz się głębiej w morskich ciemnościach...")
            time.sleep(2)
            result = functions.underwater_choice()
            if result is False:
                break
        elif inp == "b":
            print("=="*30)
            for k, v in player.items():
                time.sleep(1)
                print(f"{k} ----- {v}")
        elif inp == "c":
            print("Wracasz na powierzchnię...")
            return True
        else:
            print("Niepoprawnie wpisana komenda!")
        if player["hp"] <= 0:
            break
    if player["hp"] <= 0:
        print("Twoja postać nie żyje!")
        return False
    
    return True