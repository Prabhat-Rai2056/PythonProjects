import random

def main():
    def hangman():

        #list of words to be asked

        list_of_words = ['hangman', 'football', 'samsung', 'guitar', 'xiomi']
        word = random.choice(list_of_words)
        turns=10
        guessmade= ''
        valid_entry = set('abcdefghijklmnopqrstuvwxyz')
        while len (word)>0:
            main_word = ""

#check the correct word

            for letter in word:
                if letter in guessmade:
                    main_word = main_word+letter
                else:
                    main_word = main_word+"_"

            if main_word == word:
                print(main_word)
                print("you won!!!!!")
                r = input("do you want to restart the game, y for yes and n for no: ")
                if r == "y":
                    main()
                elif r == "n":
                    quit()

            print("guess the words ", main_word)
            guess=input()

            if guess in guessmade:
                print("you already guessed that letter!!!")

            if guess not in valid_entry:
                print("enter valid character")
                guess=input()

            if guess in valid_entry:
                guessmade = guessmade + guess
                if guess not in word:
                    turns = turns-1

#check the turn

                    if turns == 9:
                        print("9 turns left!!!!")
                        print("___________________")
                    if turns == 8:
                        print("8 turns left!!!!")
                        print("___________________")
                        print("          o        ")
                    if turns == 7:
                        print("7 turns left!!!!")
                        print("___________________")
                        print("          o        ")
                        print("          |        ")
                    if turns == 6:
                        print("6 turns left!!!!")
                        print("___________________")
                        print("          o        ")
                        print("          |        ")
                        print("         /         ")
                    if turns == 5:
                        print("5 turns left!!!!")
                        print("___________________")
                        print("          o        ")
                        print("          |        ")
                        print("         / \       ")
                    if turns == 4:
                        print("4 turns left!!!!")
                        print("___________________")
                        print("        \ o        ")
                        print("          |        ")
                        print("         / \       ")
                    if turns == 3:
                        print("3 turns left!!!!")
                        print("___________________")
                        print("        \ o /       ")
                        print("          |        ")
                        print("         / \       ")
                    if turns == 2:
                        print("2 turns left!!!!")
                        print("___________________")
                        print("        \ o /  |   ")
                        print("          |        ")
                        print("         / \       ")
                    if turns == 1:
                        print("only 1 turns left!!!! hangman on last breath")
                        print("___________________")
                        print("        \ o /__|   ")
                        print("          |        ")
                        print("         / \       ")
                    if turns == 0:
                        print("___________________")
                        print("          o __|    ")
                        print("         /|\      b")
                        print("         / \       ")
                        print("you loose!")
                        print("man is hanged!!!")
                        r = input("do you want to restart the game, y for yes and n for no: ")
                        if r == "y":
                            main()
                        elif r == "n":
                            quit()


                        quit()

    #enter name

    name = input("Enter your name:")
    print("welcome", name, "!")
    print("_________________________")
    print("try to guess the word in less than 10 attempts")
    hangman()
main()