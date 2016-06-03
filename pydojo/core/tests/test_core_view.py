import pytest
from flask import url_for
from mock import patch

from pydojo.core.tests.test_utils import count_words
from pydojo.core.forms import CodeEditorForm


@pytest.mark.usefixtures('client_class')
class TestCoreIndexView:

    def test_get_status_code(self):
        response = self.client.get(url_for('core.index'))
        assert response.status_code == 302


@pytest.mark.usefixtures('client_class')
class TestCoreEditorView:

    # pseudo acceptance test
    @patch('pydojo.core.views.id_generator')
    def test_html(self, mock_id_generator):
        mock_id_generator.return_value = "Rafael1234"
        url = url_for('core.editor', hashkey="Rafael1234")
        response = self.client.get(url)
        form_url = url_for('core.editor', hashkey="Rafael1234")
        tags = (
            ('<title>', 1),
            ('<form action="{}".*method="post"'.format(form_url), 1),
            ('<input id="csrf_token" name="csrf_token" type="hidden".*', 1),
            ('<input id="hashkey" name="hashkey" '
                'type="hidden" value="Rafael1234">', 1),
            ('<textarea.*id="code".*</textarea>', 1),
            ('<button type="submit".*</button>', 1),
            ('<script src="/static/js/jquery.min.js"></script>', 1),
            ('<script src="/static/js/bootstrap.min.js"></script>', 1),
            ('<link href="/static/css/bootstrap.min.css".*>', 1),
            ('<link href="/static/css/bootstrap-theme.min.css".*>', 1),
        )
        content = response.data.decode('utf-8')
        for text, count in tags:
            assert count_words(text, content) == count

    @patch('pydojo.core.views.id_generator')
    def test_return_correct_url_hash(self, mock_id_generator):
        mock_id_generator.return_value = "Rafael1234"
        response = self.client.get(url_for('core.index'))
        expected_url = url_for('core.editor', hashkey="Rafael1234")
        assert expected_url in response.location

    def test_correct_post(self):
        url = url_for('core.editor', hashkey="Rafael1234")
        response = self.client.post(url, data={
            'hashkey': 'Rafael1234',
            'source_code': 'print("Hello World!")'
        })
        assert response.status_code == 200
