import json
import random
import sshme

from classes import Question


def load_data():
    with open('data.json') as file:
        data = json.load(file)

    questions = [Question(question=i['q'], point=int(i['d']), correct_answer=i['a']) for i in data]

    random.shuffle(questions)

    return questions


def print_stat(correct_count, questions_count, total_point):
    print(f"Вот и всё!\nОтвечено {correct_count} вопроса из {questions_count}\nНабрано баллов: {total_point}")


def main():
    correct_count = 0
    total_point = 0
    questions = load_data()

    for question in questions:
        user_answer = input(question.build_question())
        question.user_answer = user_answer
        if question.is_correct():
            print(question.build_positive_feedback())

            correct_count += 1
            total_point += question.get_points()
        else:
            print(question.build_negative_feedback())

    print_stat(correct_count, len(questions), total_point)


if __name__ == '__main__':
    main()
