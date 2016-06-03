import pytest
from pydojo.core.forms import CodeEditorForm
from pydojo.core.models import SourceCode


@pytest.mark.usefixtures('client_class')
class TestCodeEditorForm:

    def test_create_form_valid(self):
        data = {'code': 'print("Hello!")', 'hashkey': 'Rafael123'}
        form = CodeEditorForm(data=data)
        assert form.validate()

    def test_create_form_invalid(self):
        data = {'code': '', 'hashkey': 'Rafael123'}
        form = CodeEditorForm(data=data)
        assert not form.validate()

    def test_save(self, db):
        data = {'code': 'print("Hello!")', 'hashkey': 'Rafael123'}
        form = CodeEditorForm(data=data)
        form.save()
        assert SourceCode.query.count() == 1
