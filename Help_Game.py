def help_game():
    need_help = True
    help = input("Brauchst du eine kleine Regelauffrischung oder spielst diese Version zum ersten Mal (J/N)?: ").lower()

    while need_help is True:
        if help != "j":
            need_help = False
        else:
            print("Kein Problem, ich erkläre dir die Regeln gerne!\n"
                  "Ziel des Spiels ist es drei Kreuze in einer Reihe zu bekommen.\n"
                  "Dabei ist es egal ob diese waagerecht, senkrecht oder diagonal angeordnet sind.\n"
                  "Dein Kreuz setzt du durch eine Koordinatenangabe. Das Feld setzt sich aus 3 Reihen mit jeweils 3 Feldern zusammen.\n"
                  'Bei der Eingabe "A3" wird dein Kreuz in die obersten Reihe ganz rechts gesetzt. Bei der Eingabe "B2" genau in der Mitte des Feldes.')

            help_again = input("Möchtest du die Regeln noch einmal hören (J/N)?: ").lower()
            if help_again == "n":
                need_help = False

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ß", "Ä", "Ö", "Ü"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specials = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", " "]


