import graphene
from blog.resolvers.queries import Query as BlogQuery
from blog.resolvers.mutations import Mutation as BlogMutation
from account.resolvers.mutations import Mutation as AccountMutation

class Mutation(BlogMutation, AccountMutation):
    pass

class Query(BlogQuery):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)