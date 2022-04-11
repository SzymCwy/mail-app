import datetime

from rest_framework import serializers
from .models import Mailbox, Template, Email
from .tasks import send_mail
import logging

logger = logging.getLogger(__name__)


class Mailbox_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = ['host', 'port', 'login', 'password', 'email_from', 'use_ssl', 'is_active', 'last_update', 'sent']


class Template_serializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class Email_serializerCreate(serializers.ModelSerializer):

    to1 = serializers.CharField(required=True, label='To:', help_text='Add email and separate them by ","')
    cc1 = serializers.CharField(required=False, label='Cc:', help_text='Add email and separate them by ","')
    bcc1 = serializers.CharField(required=False, label='Bcc:', help_text='Add email and separate them by ","')

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
            is_sent = None
            for i in range(3):
                if send_mail(validated_data):
                    is_sent = True
                    validated_data['sent_date'] = datetime.date.today()
                    logger.warning('Email sent!')
                    return Email.objects.create(**validated_data)
                else:
                    is_sent = False
                    logger.warning('Email not sent!')
            if is_sent is False:
                validated_data['sent_date'] = None
                print(validated_data)
                return Email.objects.create(**validated_data)
        else:
            raise serializers.ValidationError('Account is not active')


class EmailList(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
