import graphene
from django.contrib.auth import get_user_model
from .queryTypes import UserType
from account.models import User
from datetime import datetime

class UserRegistrationMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birth = graphene.String(required=False)  # Accept birthdate as a string in ISO 8601 format

    def mutate(self, info, email, password, first_name, last_name, birth=None):
        birthdate = None
        if birth:
            # Parse the birthdate string into a datetime object
            birthdate = datetime.fromisoformat(birth.replace('Z', '+00:00'))

        # Create the user object
        user = User(
            email=email,
            birth=birthdate,  # Replace 'birthdate' with the actual field in your model
            is_active=False,
            username=email,  # Set username directly
            first_name=first_name,
            last_name=last_name,
        )

        # Set the password
        user.set_password(password)

        # Save the user
        user.save()

        # Return the mutation result
        return UserRegistrationMutation(user=user)

class Mutation(graphene.ObjectType):
    register_user = UserRegistrationMutation.Field()