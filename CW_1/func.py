import random

MORZE_CODE = {
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
def morse_encode(word):
  encode = ''
  for i in word:
    encode += MORZE_CODE[i]

  return encode


def get_word(words):
  return random.choice(words)

def print_statistics(answers): # answers = [True, False, True, True]
  wrong_count = 0
  for i in answers:
    if not i:
      wrong_count += 1


  print(f"Всего задачек: {len(answers)}\n",
        f"Отвечено верно: {answers.count(True)}\n",
        f"Отвечено неверно: {wrong_count}\n")

if __name__ == '__main__':
  print('Я главный')