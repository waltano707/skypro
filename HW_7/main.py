from utils import *


def main():
    student_pk = int(input("Введите номер студента"))

    if student := get_student_by_pk(student_pk):
        print(f"Студент: {student['full_name']}")
        print(f"Знает: {student['skills']}")
    else:
        print('У нас нет такого студента')
        return

    professional_title = input(f"Выберите специальность для оценки студента {student['full_name']}")
    if professional := get_profession_by_title(professional_title):
        result = check_fitness(student, professional)

        print(f"Пригодность: {result['fit_percent']}")
        print(f"{student['full_name']} знает: {result['has']}")
        print(f"{student['full_name']} не знает: {result['lacks']}")
    else:
        print('У нас нет такой специальности')
        return


if __name__ == '__main__':
    main()
