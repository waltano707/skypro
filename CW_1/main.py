from func import *

WORDS = ['code', 'bit']






def main():
  input("Сегодня мы потренируемся расшифровывать азбуку Морзе\n" + \
        "Нажмите Enter и начнем")
  answers = []
  for i in range(1,6):
    word = get_word(WORDS)
    encode_word = morse_encode(word)

    answer = input(f"Слово {i} – {encode_word}")
    if answer == word:
      print(f'Верно, {word}!')
      answers.append(True)
    else:
      print(f'Неверно, {word}')
      answers.append(False)
  print_statistics(answers)



if __name__ == '__main__':
  main()