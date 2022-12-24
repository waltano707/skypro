from flask import Blueprint, render_template, request, redirect, url_for

from loader.utils import save_uploaded_file, save_post

loader_bp = Blueprint('loader_blueprint', __name__, template_folder='templates')


# @loader_bp.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     if request.method == "GET":
#         return render_template('post_form.html')
#     elif request.method == "POST":
#         file = request.files.get("picture")
#         content = request.form.get("content")
#
#         if file is None or content is None:
#             return "Переданы не все данные"
#
#         url = save_uploaded_file(file)
#         save_post(content, url)
#
#         return redirect("/")


@loader_bp.route("/post", methods=["GET"])
def page_post_form_show():
    return render_template('post_form.html')


@loader_bp.route("/post_url", methods=["POST"])
def page_post_form_add():

    file = request.files.get("picture")
    content = request.form.get("content")

    if file is None or content is None:
        return "Переданы не все данные"

    url = save_uploaded_file(file)
    save_post(content, url)

    return redirect(url_for('main_blueprint.page_index'))
