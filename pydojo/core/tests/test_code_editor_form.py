import pytest
from pydojo.core.forms import CodeEditorForm


@pytest.mark.usefixtures('client_class')
class TestCodeEditorForm:

    def test_create_form_valid(self):
        data = {'source_code': 'print("Hello!")'}
        form = CodeEditorForm(data=data)
        assert form.validate()

    def test_create_form_invalid(self):
        data = {'source_code': ''}
        form = CodeEditorForm(data=data)
        assert not form.validate()
