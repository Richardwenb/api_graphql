from flask import Flask
from graphene import ObjectType, String, List, Schema
from flask_graphql import GraphQLView

app = Flask(__name__)

class News(ObjectType):
    title = String()
    content = String()

class Query(ObjectType):
    news = List(News)

    def resolve_news(self, info):
        fake_news = [
            {"title": "Santos vence a partida", "content": "O time Santos venceu por 2-0."},
            {"title": "Nova contratação para o Santos", "content": "Santos contrata novo jogador."},
        ]
        return [News(title=news["title"], content=news["content"]) for news in fake_news]

schema = Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
