from utils import *
import os

WORDS_FILE = os.path.join("data", "words.txt")
HISTORY_FILE = os.path.join("data", 'history.txt')


def main():
    print("Программа: Введите ваше имя")
    user_name = input("Пользователь:")

    words = read_data(WORDS_FILE)
    point = 0
    for i, word in enumerate(words):
        encoded_word = shuffle_word(word)
        user_answer = input(f"Программа: Угадайте слово: {encoded_word}")
        if user_answer == word:
            point += 10
            print("Программа: Верно! Вы получаете 10 очков.")
        else:
            print(f"Программа: Неверно! Верный ответ – {word}.")

    write_result(user_name, point, HISTORY_FILE)
    print_history(HISTORY_FILE)


if __name__ == "__main__":
    main()
