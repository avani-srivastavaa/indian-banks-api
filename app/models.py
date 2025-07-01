from app import db

class Bank(db.Model):
    __tablename__ = 'banks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    branches = db.relationship('Branch', backref='bank', lazy=True)

class Branch(db.Model):
    __tablename__ = 'branches'

    id = db.Column(db.Integer, primary_key=True)
    ifsc = db.Column(db.String, unique=True, nullable=False)
    branch = db.Column(db.String)
    address = db.Column(db.String)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)

