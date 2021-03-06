
from graphene import relay
from django.contrib.auth import get_user_model
from cart.models import Cart

from graphene_django import DjangoObjectType

user = get_user_model()


class CartType(DjangoObjectType):
    class Meta:
        model = Cart
        interfaces = (relay.Node,)
