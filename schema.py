import graphene

class News(graphene.ObjectType):
    title = graphene.String()
    content = graphene.String()

class Query(graphene.ObjectType):
    news = graphene.List(News)

    def resolve_news(self, info):
        fake_news = [
            {"title": "Santos vence a partida", "content": "O time Santos venceu por 2-0."},
            {"title": "Nova contratação para o Santos", "content": "Santos contrata novo jogador."},
        ]
        return [News(title=news["title"], content=news["content"]) for news in fake_news]

schema = graphene.Schema(query=Query)
