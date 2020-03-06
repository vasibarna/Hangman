from hangman import Hangman
from random_word import magic_word
from hangman_sketches import game_images

word = magic_word()
attempts = 7

if __name__ == "__main__":
    print(f"\nLet's play Hangman. Your word is:\n")
    game = Hangman(word)
    game_images(game.attempts)

    game.show_hidden_word(word[0])
    print(game.show_hidden_word(word[-1]))
    game.tried_letters.extend([word[0], word[-1]])
    print(f"First and last letter are shown in the word as default: {game.tried_letters}")
    while game.attempts < attempts:
        letter = game.user_input()
        if game.invalid_user_input(letter):
            print("Try a valid letter!")
            continue
        if letter in game.tried_letters:
            print("Try another one!")
            continue
        else:
            game.tried_letters.append(letter)
        print(f"Letters already tried: {game.tried_letters}")
        if letter in game.word:
            print(game.show_hidden_word(letter))
            print(f"You have {7 - game.attempts} attempts")
            # if "_" not in game.show_hidden_word(letter):
            if game.has_won():
                print("Game Over. You won this game!")
                break
        else:
            game.attempts += 1
            game_images(game.attempts)
            print(" ".join(game.hidden_word))
            if game.attempts == 7:
                print(f"Game Over. You lost this game! The magic word was: < {word} >")
                break

