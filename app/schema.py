import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Bank, Branch

class BankType(SQLAlchemyObjectType):
    class Meta:
        model = Bank
        interfaces = (relay.Node,)

class BranchType(SQLAlchemyObjectType):
    class Meta:
        model = Branch
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    branches = SQLAlchemyConnectionField(BranchType.connection)
    banks = SQLAlchemyConnectionField(BankType.connection)

schema = graphene.Schema(query=Query)
