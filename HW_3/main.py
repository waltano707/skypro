questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]


print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
user_answer = input()

correct = 0
total_point = 0

if user_answer.lower() == 'ready':
  for i, question in enumerate(questions):

    for j in range(3):
      print(question)
      if input().lower() == answers[i]:
        correct += 1
        total_point += 3 - j
        print("Ответ верный!")
        break;
      elif 2 - j != 0:
        print(f"Попробуйте еще")
        print(f"У вас осталось {2 - j} попыток")
      else:
        print(f"Увы, но нет. Верный ответ: {answers[i]}")


  print(f"Вот и все! Вы ответили на {correct} вопросов из {len(questions)} верно, это {round(correct/len(questions)*100)} процентов.")
  print(f"Заработано очков {total_point}")
else:
  print("Кажется, вы не хотите играть. Очень жаль")


