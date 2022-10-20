import random
morse_dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

#words = ["bit", "code", "test"]
words = input("Введите слова для игры через побел").split()
print(words)

def code_morse(word):
  return " ".join([morse_dict[i] for i in word])  


def get_word(words):
  return random.choice(words)


def print_statistics(answers):
  print(f"Всего задачек: {len(answers)}\n",
        f"Отвечено верно: {answers.count(True)}\n",
        f"Отвечено неверно: {answers.count(False)}")


answers = []

for i in range(5):
  word = get_word(words)
  user_answer = input(f"Попробуйте угадать слово : {code_morse(word)}")
  if user_answer.lower().strip() == word:
    print(f"Вы угадали: {word}")
    answers.append(True)
  else:
    print(f"Неверно: {word}")
    answers.append(False)


print_statistics(answers)