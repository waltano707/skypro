import json


def load_posts(name):
    try:

        with open('posts.json', encoding='utf-8') as file:
            data = json.load(file)

        return [post for post in data if name.lower() in post['content'].lower()]

    except FileNotFoundError as e:
        with open('posts.json', encoding='utf-8', mode='w') as file:
            json.dump([], file)

        return []
