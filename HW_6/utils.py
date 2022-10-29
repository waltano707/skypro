import random


def read_data(file_name):
    words = []
    # with open('words.txt', 'r', encoding='utf-8') as words_data:
    #     while line := words_data.readline():
    #         words.append(line.replace("\n", ""))
    # return words
    with open(file_name, 'r', encoding='utf-8') as words_data:
        words = words_data.readlines()

    for i, word in enumerate(words):
        words[i] = word.replace("\n", "")

    return words


def write_result(user_name, score, history_file):
    with open(history_file, 'a', encoding='utf-8') as history_data:
        history_data.write(f"{user_name} {score}\n")


def shuffle_word(word):
    chars = list(word)

    random.shuffle(chars)
    return "".join(chars)


def print_history(history_file):
    data = read_data(file_name=history_file)

    total_game = 0
    best_score = 0
    for row in data:
        total_game += 1
        row_data = row.split(" ")
        if int(row_data[1]) > best_score:
            best_score = int(row_data[1])

    print(f"Всего игр сыграно: {total_game}")
    print(f"Максимальный рекорд: {best_score}")
