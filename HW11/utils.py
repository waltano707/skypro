import json


def load_data(file_name):
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)

    return data


def load_candidates():
    return load_data('data.json')


def get_candidate(candidate_id):
    for candidate in load_candidates():
        if candidate['id'] == int(candidate_id):
            return candidate


def get_candidates_by_name(candidate_name):
    candidates = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name):
    return [candidate for candidate in load_candidates() if skill_name.lower() in candidate['skills'].lower()]
