words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

level = input("Выберите уровень сложности.\nЛегкий, средний, сложный.").lower()

if level == 'легкий':
    words = words_easy
    print("Выбран легкий уровень сложности, мы предложим 5 слов, подберите перевод.")
elif level == 'средний':
    words = words_medium
    print("Выбран средний уровень сложности, мы предложим 5 слов, подберите перевод.")
elif level == 'сложный':
    words = words_hard
    print("Выбран сложный уровень сложности, мы предложим 5 слов, подберите перевод.")
else:
    quit()

correct_words = []
wrong_words = []

for key, value in words.items():
    answer = input(f"{key}, {len(value)} букв, начинается на {value[0]}...").lower()
    if answer == value:
        print("Верно")
        correct_words.append(value)
    else:
        print(f"Неверно.  Правильный ответ: {value}")
        wrong_words.append(value)

print(f"Ваш уровень: {levels[len(correct_words)]}")

print("Угадали:")
for i in correct_words:
    print(i)

print("Не угадали:")
for i in wrong_words:
    print(i)

