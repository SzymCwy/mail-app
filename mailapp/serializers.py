from rest_framework import serializers
from .models import Mailbox, Template, Email
from .tasks import send_mail


class Mailbox_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = ['host', 'port', 'login', 'password', 'email_from', 'use_ssl', 'is_active', 'date',
                  'last_update', 'sent']


class Template_serializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class Email_serializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['mailbox', 'template', 'to', 'reply_to', 'sent_date', 'date']

    def create(self, validated_data):
        send_mail(validated_data)
        return Email.objects.create(**validated_data)
