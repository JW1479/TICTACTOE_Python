#Module importieren
import random
from Help_Game import help_game, alphabet, numbers, specials
import time

#Win-Condition:
def check_win(player):
    global game_ongoing
    if playing_field[0][0] == playing_field[1][0] == playing_field[2][0] != "_" or \
       playing_field[1][0] == playing_field[1][1] == playing_field[1][2] != "_" or \
       playing_field[2][0] == playing_field[2][1] == playing_field[2][2] != "_" or \
       playing_field[0][0] == playing_field[0][1] == playing_field[0][2] != "_" or \
       playing_field[0][1] == playing_field[1][1] == playing_field[2][1] != "_" or \
       playing_field[0][2] == playing_field[1][2] == playing_field[2][2] != "_" or \
       playing_field[0][0] == playing_field[1][1] == playing_field[2][2] != "_" or \
       playing_field[0][2] == playing_field[1][1] == playing_field[2][0] != "_":
        print(f"{player} hat gewonnen!")
        game_ongoing = False
    if turns_available == []:
        print("Das Spiel ist unendschieden!")
        game_ongoing = False


# Züge:
def turn_computer():
    if not turns_available == []:
        computer_choice = random.choice(turns_available)
        computer_letter_position = int(letters_row.index(computer_choice[0]))
        computer_number_position = int(computer_choice[1]) - 1
        turns_available.remove(computer_choice)
        print(f"Der Computer setzt seinen Kreis auf das Feld: {computer_choice}")
        playing_field[computer_letter_position][computer_number_position] = "O"
        show_field()

def turn_player():
    if not turns_available == []:
        print("Du bist nun am Zug!")
        user_choice = input("Wo möchtest du dein Kreuz setzen? ").upper()

        #Falsche Eingabe an Position 1
        if len(user_choice) == 0:
            print("Bitte mache deine Eingabe (Zuerst der Buchstabe, dann die Zahl) und drücke dann erst Enter.")
            turn_player()
        if user_choice[0] != "A" and user_choice[0] != "B" and user_choice[0] != "C":
            for element in alphabet:
                if user_choice[0] in alphabet:
                    print("Du hast einen falschen Buchstaben, eingegeben, der außerhalb des Feldes liegt! Versuchs A, B oder C.")
                    turn_player()
                elif user_choice[0] in numbers:
                    print("Du hast die Zahl an die falsche Stelle gesetzt, schreibe bitte zuerst den Buchstaben (A, B, C).")
                    turn_player()
                elif user_choice[0] in specials:
                    print("Du hast wohl ein Sonderzeichen eingegeben, gib bitte A, B oder C ein.")
                    turn_player()
        #Falsche Eingabe an Position 2
        if len(user_choice) == 1:
            print("Bitte gib für die zweite Stelle eine Zahl (1, 2, 3) ein und lasse diese nicht leer.")
            turn_player()
        elif len(user_choice) >= 3:
            print("Bitte gib nur einen Buchstaben und eine einstellige Zahl als Eingabe ein.")
            turn_player()
        elif user_choice[1] != 1 and user_choice[1] != 2 and user_choice[1] != 3:
            if user_choice[1] in alphabet:
                print("Du hast einen Buchstaben an die falsche stelle gesetzt, schreib als zweites bitte die Zahl (1, 2, 3)")
                turn_player()
            elif user_choice[1] in specials:
                print("Du hast ein Sonderzeichen eingegeben, gib bitte 1, 2 oder 3 ein.")
                turn_player()
            elif int(user_choice[1])-1 >= 3:
                print("Du hast eine zu große Zahl eingegeben, die außerhalb des Feldes liegt. Versuch 1, 2 oder 3.")
                turn_player()
            elif int(user_choice[1])-1 < 0:
                print("Du hast eine zu kleine Zahl eingegeben, die außerhalb des Feldes liegt. Versuch 1, 2 oder 3.")
                turn_player()


        else:
            player_letter_position = int(letters_row.index(user_choice[0]))
            player_number_position = int(user_choice[1]) - 1
        #Feld bereits belegt?
            if playing_field[player_letter_position][player_number_position] == "_":
                playing_field[player_letter_position][player_number_position] = "X"
                turns_available.remove(user_choice)
                show_field()
            else:
                print("Dieses Feld ist bereits belegt! Versuch ein anderes!")
                turn_player()
                show_field()

#Spiel-Ablauf
#Willkommensnachricht, Regeln und "Wer beginnt?"
print("Willkommen bei Tic-Tac-Toe!")
help_game()
name_player = input("Bitte gib deinen Namen ein: ")
players = [name_player, "Der Computer"]
while True:
    game_ongoing = True

    # Spielfeld erstellen
    row1 = ["_", "_", "_"]
    row2 = ["_", "_", "_"]
    row3 = ["_", "_", "_"]
    letters_row = ["A", "B", "C"]
    playing_field = [row1, row2, row3]
    turns_available = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    def show_field():
        print(f"{row1}\n{row2}\n{row3}\n")

    beginner = random.choice(players)
    print(f"{beginner} darf den ersten Zug machen!")

    #Spielreihenfolge

    show_field()

    while game_ongoing:
        if beginner == name_player:
            turn_player()
            check_win(name_player)
            time.sleep(1)
            if not game_ongoing:
                break
            turn_computer()
            check_win("Der Computer")
            time.sleep(1)
            if not game_ongoing:
                break

        else:
            turn_computer()
            check_win("Der Computer")
            time.sleep(1)
            if not game_ongoing:
                break
            turn_player()
            check_win(name_player)
            time.sleep(1)
            if not game_ongoing:
                break

    again = input("Möchtest du noch einmal spielen (J/N)?: ").upper()
    if again == "J":
        continue
    else:
        print(f"\nSchade, aber vielleicht ein anderes Mal! :)\nIch wünsche dir noch einen schönen Tag, {name_player}!")
        time.sleep(4)
        exit()



