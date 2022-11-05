import json
import os


def load_students():
    with open(os.path.join('data', 'students.json'), mode='r', encoding='utf-8') as file:
        students = json.load(file)

    return students


def load_professions():
    with open('data/professions.json', mode='r', encoding='utf-8') as file:
        professions = json.load(file)

    return professions


def get_student_by_pk(pk):
    for student in load_students():
        if student['pk'] == pk:
            return student
    # raise Exception('student not found')


def get_profession_by_title(title):
    for prof in load_professions():
        if prof['title'] == title:
            return prof


def check_fitness(student, profession):
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])

    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills.difference(student_skills)

    return {
        "has": list(has_skills),
        "lacks": list(lacks_skills),
        "fit_percent": len(has_skills) / len(set(profession_skills)) * 100
    }
