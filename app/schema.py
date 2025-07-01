import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Bank, Branch
from app import db

# ✅ Basic GraphQL types
class BankType(SQLAlchemyObjectType):
    class Meta:
        model = Bank

class BranchType(SQLAlchemyObjectType):
    class Meta:
        model = Branch

# ✅ Root query
class Query(graphene.ObjectType):
    all_banks = graphene.List(BankType)
    all_branches = graphene.List(BranchType)

    def resolve_all_banks(self, info):
        return db.session.query(Bank).all()

    def resolve_all_branches(self, info):
        return db.session.query(Branch).all()

schema = graphene.Schema(query=Query)
