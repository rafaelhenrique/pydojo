from pydojo.ext import db


class SourceCode(db.Model):
    id = db.Column(db.BigInteger, nullable=False, unique=True,
                   autoincrement=True, primary_key=True)
    hashkey = db.Column(db.String(10), unique=True, nullable=False)
    code = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "SourceCode(%r, '%r', '%r')" % (self.id, self.hashkey,
                                               self.code[0:10])
