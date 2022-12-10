import json


def load_candidates():
    with open("data.json", "r", encoding='utf-8') as f:
        data = json.load(f)

    return data


def load_candidate(pk):
    for obj in load_candidates():
        if obj['id'] == pk:
            return obj


def load_candidate_by_skill(skill):
    return [obj for obj in load_candidates() if skill.lower().strip() in obj['skills']]
