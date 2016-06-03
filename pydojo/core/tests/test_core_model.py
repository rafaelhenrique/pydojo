from pydojo.core.models import SourceCode


class TestSourceCodeModel:

    def test_create_valid_source_code(self, db):
        source_code = SourceCode(hashkey="Rafael123",
                                 code="print('Hello World!')")
        db.session.add(source_code)
        db.session.commit()
        assert SourceCode.query.count() == 1
