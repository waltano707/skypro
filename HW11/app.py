from flask import Flask, render_template

from utils import load_candidates, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def show_candidates():
    candidates = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def show_candidate(id):
    candidate = get_candidate(id)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<name>")
def show_candidate_by_name(name):
    candidates = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<skill>")
def show_candidate_by_skill(skill):
    candidates = get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=candidates, skill=skill)


if __name__ == '__main__':
    app.run(debug=True)
