from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class CodeEditorForm(Form):
    source_code = TextAreaField('source_code', validators=[DataRequired()])
