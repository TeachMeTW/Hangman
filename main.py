# Hanging the man

import random

def maingame():
    message = 'Welcome to the game! You know how hangman works... I don\'t need to explain this simple game' 
    
    print(message)
    print("Would you like to play?\n")
    play = True
    yesorno = input("Yes or nah: \n")
    # Simple question
    if yesorno == "Yes" or yesorno == "yes" or yesorno == "yea":
        play = True
        print("\nWelcome to Hanging the Man")
        
    else:
        play = False
        print("Ok then")
        
    
    while play == True:
        print("\nGame Starting....")
        words = [
            "Despacito", "Gamer", "Dab", "YourMom", "NaeNae", "cope", "roblox", "minecraft", "ratio", "cringe"
        ]
        # Words list, can be changed
        chosen = random.choice(words).lower() # chooses a random word | lowercase
        player_guess = None # placeholder
        letter_guess = [] # letters guessed by player
        words_guess = [] # words to be guessed | ------
        for letter in chosen:
            words_guess.append("-")
        joined = None # placeholder
        attempts = 6
        while (attempts != 0 and "-" in words_guess):
            print(f"\nYou have {attempts} guesses remaining")
            joined = "".join(words_guess) # prints out the number of blanks
            print(joined)

            try:
                player_guess = str(input("\nSelect a letter...\n")).lower()
            except:
                print("\nThats not valid...")
                continue
            else:
                if not player_guess.isalpha():
                    print("\nBoi this aint a letter... try again...")
                    continue
                elif len(player_guess) > 1:
                    print("\nOne letter only...")
                    continue
                elif player_guess in letter_guess:
                    print("\nYou've guessed that already...")
                    continue
                else:
                    pass

            letter_guess.append(player_guess)

            for letter in range(len(chosen)): # quite confusing
                if player_guess == chosen[letter]:
                    words_guess[letter] = player_guess

            if player_guess not in chosen:
                attempts -= 1
                print("\nOof...guess again")

        if "-" not in words_guess:
            print(("\nCongrats {} was correct").format(chosen))
        else:
            print(("\nOof the word was supposed to be {}.").format(chosen))

        print("\nPlay again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play = False

maingame()