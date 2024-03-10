import graphene
from graphene_django import DjangoObjectType
from .queryTypes import GetUserType
from ..models import User

class Query(graphene.ObjectType):
    users = graphene.List(GetUserType)
    question_by_id = graphene.Field(GetUserType, id=graphene.String())

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)