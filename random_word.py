import random

file = "word_list"

def magic_word():
    with open(file, "r") as f:
        line = f.readline()
        word_list = []
        while line:
            line = f.readline()
            word_list.append(line.strip())
    index = random.randint(0, len(word_list)-1)
    return word_list[index]


if __name__ == "__main__":
    print(magic_word())