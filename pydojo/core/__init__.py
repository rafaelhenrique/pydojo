from flask import Blueprint

core_blueprint = Blueprint('core', __name__, template_folder='templates',
                           static_folder='static', static_url_path='core')

from pydojo.core import views  # noqa
from pydojo.core import models  # noqa
