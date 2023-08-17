import graphene
from graphene import ObjectType, String
from graphene import Schema
from flask_graphql import GraphQLView
from app import *


class Query(graphene.ObjectType):
    noticia = graphene.String()

    def resolve_noticia(self, info):
        return "Bolsa de valores aumenta em 30%"

    schema = Schema(query=Query)
schema = graphene.Schema(query=Query)