from rest_framework import serializers
from .models import Mailbox, Template, Email


class Mailbox_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = ['sent']
