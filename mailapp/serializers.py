from rest_framework import serializers
from .models import Mailbox, Template, Email
from .tasks import send_mail
import logging

logger = logging.getLogger(__name__)


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

    to1 = serializers.CharField(required=True, label='To:', help_text='Add email and separate them by ","', source='to')
    cc1 = serializers.CharField(required=False, label='Cc:', help_text='Add email and separate them by ","',
                                source='cc')
    bcc1 = serializers.CharField(required=False, label='Bcc:', help_text='Add email and separate them by ","',
                                 source='bcc')

    class Meta:
        model = Email
        fields = ['to1', 'cc1', 'bcc1', 'mailbox', 'template', 'reply_to']

    def create(self, validated_data):

        """As array fields can not be shown in HTML I create 3 temporary char fields, convert them into arrays and put
        to create"""
        field_list = ['to', 'cc', 'bcc']

        for field in field_list:
            try:
                validated_data[f'{field}'] = self.data[f'{field}1'].split(',')
                del validated_data[f'{field}1']
            except KeyError:
                validated_data[f'{field}'] = None

        if validated_data.get('mailbox').is_active:
            if send_mail(validated_data):
                logger.warning('Email sent!')
                return Email.objects.create(**validated_data)
            else:
                raise serializers.ValidationError('Wrong credentials')
        else:
            raise serializers.ValidationError('Account is not active')
