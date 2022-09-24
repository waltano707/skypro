
# ШАГ 1
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


user_name = input(bcolors.WARNING +
    "Привет! Предлагаю проверить свои знания английского!\n" +
    "Расскажи, как тебя зовут!"
)

print(bcolors.OKGREEN + f"Привет, {user_name}, начинаем тренировку!")

correct = 0

# Ввод первого вопроса
user_answer = input("My name ___ Vova\n")
if user_answer == "is":
  correct += 1
  print("Ответ верный!")
else:
  print("Неправильно.Правильный ответ: is")

user_answer = input("I ___ a coder\n")
if user_answer == "am":
  correct += 1
  print("Ответ верный!")
else:
  print('\\Неправильно.Правильный ответ: am')

user_answer = input("I live ___ Moscow\n")
if user_answer == "in":
  correct += 1
  print("Ответ верный!")
else:
  print("Неправильно.Правильный ответ: in")

total_point = correct * 10
print(
    f"Вот и все, {user_name}!\n" +
    f"Вы ответили на {correct} вопросов из 3 верно.\n" +
    f"Вы заработали {total_point} баллов.\n" +
    f"Это {total_point/30*100:.2f} : {round(total_point/30*100, 2)} процентов."
)
