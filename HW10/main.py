from flask import Flask

from utils import load_candidates, load_candidate, load_candidate_by_skill

app = Flask(__name__)


@app.route("/")
def main():
    candidates = load_candidates()

    candidates_str = ''
    for candidate in candidates:
        candidate_str = f"Имя кандидата: {candidate['name']}<br>" \
                        f"Позиция кандидата: {candidate['position']}<br>" \
                        f"Навыки через запятую: {candidate['skills']}<br><br>"
        candidates_str += candidate_str

    return f"<pre>{candidates_str}</pre>"


@app.route("/candidate/<int:pk>")
def view_candidate(pk):
    candidate = load_candidate(pk)

    if candidate:
        candidate_str = f"Имя кандидата: {candidate['name']}<br>" \
                        f"Позиция кандидата: {candidate['position']}<br>" \
                        f"Навыки через запятую: {candidate['skills']}<br><br>"

        return f"<pre><img src=\"{candidate['picture']}\"><br>{candidate_str}</pre>"
    else:
        return f"<pre>Кандидат не найден</pre>"


@app.route("/skill/<string:skill>")
def view_candidate_by_skill(skill):
    candidates = load_candidate_by_skill(skill)

    candidates_str = ''
    for candidate in candidates:
        candidate_str = f"Имя кандидата: {candidate['name']}<br>" \
                        f"Позиция кандидата: {candidate['position']}<br>" \
                        f"Навыки через запятую: {candidate['skills']}<br><br>"
        candidates_str += candidate_str

    return f"<pre>{candidates_str}</pre>"


app.run()
