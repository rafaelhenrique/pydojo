from flask import render_template, redirect, url_for

from pydojo.core import core_blueprint
from pydojo.core.utils import id_generator


@core_blueprint.route('', methods=['GET', ])
def index():
    hashkey = id_generator()
    return redirect(url_for('core.editor', hashkey=hashkey))


@core_blueprint.route('editor/<hashkey>')
def editor(hashkey):
    return render_template('index.html', hashkey=hashkey)
