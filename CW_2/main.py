from CW_2.utils import load_word
from classes import *


def main():
    user_name = input("Ввведите имя игрока")
    print(f"Привет, {user_name}!")

    user = PLayer(name=user_name)
    word = load_word()
    print(f" Составьте {word.total_words()} слов из слова {word.word.upper()}")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
    print("Поехали, ваше первое слово?")

    while user.total_answer() < word.total_words():
        user_answer = input("Введите слово")

        if user_answer in ['stop', 'стоп']:
            print("Игра окончена")
            break
        elif len(user_answer) < 3:
            print("Слова должны быть не короче 3 букв")
        elif not word.is_in_subwords(user_answer):
            print("неверно")
        elif user.is_word_used(user_answer):
            print("уже использована")
        else:
            user.add_word(user_answer)
            print("верно")

    print(f"Игра завершена, вы угадали {user.total_answer()} слов!")


if __name__ == '__main__':
    main()
