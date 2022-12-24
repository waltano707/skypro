import json

from logger import get_logger

logger = get_logger('log')


def save_uploaded_file(picture):
    filename = picture.filename
    file_type = filename.split(".")[-1]

    if file_type.lower() not in ["jpg", "jpeg", "bmp", "png"]:
        logger.error("Wrong Formate")
        raise Exception("Wrong Formate")

    picture.save(f"static/files/{filename}")

    return f"/static/files/{filename}"


def save_post(content, url):
    with open('posts.json', encoding='utf-8') as file:
        data = json.load(file)

    data.append({
        "pic": url,
        "content": content
    })
    with open('posts.json', encoding='utf-8', mode='w') as file:
        json.dump(data, file)
