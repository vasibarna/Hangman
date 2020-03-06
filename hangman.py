from string import ascii_letters


class Hangman():
    def __init__(self, word):
        self.word = word.lower()
        self.hidden_word = ["_" for letter in range((len(self.word)))]
        self.tried_letters = []
        self.attempts = 1
        
    def show_hidden_word(self, tried_letter):
        indexes = [i for i, letter in enumerate(self.word) if letter == tried_letter]
        for index in indexes:
            self.hidden_word[index] = tried_letter
        return " ".join(self.hidden_word)
        
    def user_input(self):
        user_input = input("\nType a letter: ")
        return user_input.lower()

    def invalid_user_input(self, user_input):
        return str(user_input) not in ascii_letters and len(str(user_input)) != 1 and len(str(user_input)) == 0

    def has_won(self):
        return "_" not in self.show_hidden_word(self.tried_letters[-1])

    
