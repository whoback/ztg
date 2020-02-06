import graphene


class QueryType(graphene.ObjectType):
    name = "Query"
    description = "..."

    hello = graphene.String()

    def resolve_hello(self, root, args, info):
        return "World"


schema = graphene.Schema(query=QueryType)

