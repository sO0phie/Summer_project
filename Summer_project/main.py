from technical_part import functions
from technical_part import statistics
import time

functions.introduction_to_game()

player = statistics.player
while player["hp"] > 0 and player["hp"] != 0:
    print("=="*50)
    inp = input("Co chcesz zrobić? a - eksploracja świata, b - sprawdzenie statystyk ")
    if inp == "a":
        if player.get("portal_found") == True:
            simple_choice = input("Wybierz kierunek: a - miasto, b - morze, c - przejście do portalu ")
        else:
            simple_choice = input("Wybierz kierunek: a - miasto, b - morze ")

        if functions.direction(simple_choice) is False:
            break
    elif inp == "b":
        print("=="*30)
        for k, v in player.items():
            time.sleep(1)
            print(f"{k} ----- {v}")
    else:
        print("Niepoprawnie wpisana komenda!")
        
print("Twoja postać nie żyje!")