from flask import Blueprint, render_template, request

from main.utils import load_posts

from logger import get_logger

main_bp = Blueprint('main_blueprint', __name__)

logger = get_logger('log')


@main_bp.route("/")
def page_index():
    logger.info('load main page')
    return render_template('index.html')


@main_bp.route("/search/")
def page_search():
    name = request.args.get('s', '')

    posts = load_posts(name)

    logger.info('load search page')
    return render_template('post_list.html', posts=posts, name=name)


@main_bp.route("/list")
def page_tag():
    pass
