import sys
import time


def get_formatted_name(char_name="Player Unknown"):
    return char_name.title()


def start_game():
    while True:
        print("\n Who are you? ")
        print("\n The 'Q' key is your only escape")
        char_name = input(" ")

        if char_name.lower() == 'q':
            time.sleep(1)
            print("\nVery well... ")
            time.sleep(1)
            print("Goodbye")
            break

        char_name_proper = get_formatted_name(char_name)
        print("Very well.  Ready Player " + char_name_proper)


start_game()








