from flask_wtf import Form
from wtforms import TextAreaField, HiddenField
from wtforms.validators import DataRequired

from pydojo.ext import db
from pydojo.core.models import SourceCode


class CodeEditorForm(Form):
    code = TextAreaField('source_code', validators=[DataRequired()])
    hashkey = HiddenField('hashkey', validators=[DataRequired()])

    def save(self, **extra):
        source_code = SourceCode(hashkey=self.hashkey.data,
                                 code=self.code.data, **extra)
        db.session.add(source_code)
        db.session.commit()
