from technical_part import functions
from technical_part import statistics

functions.introduction_to_game()

player = statistics.player
while player["hp"] > 0 and player["hp"] != 0:
    print("=="*50)
    simple_choice = input("Gdzie chcesz pójść? a - miasto, b - morze ")
    functions.direction(simple_choice)

print("Twoja postać nie żyje!")