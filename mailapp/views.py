from .models import Mailbox, Template, Email
from rest_framework import generics
from .serializers import Mailbox_serializer, Email_serializer, Template_serializer


class Mailbox_list(generics.ListAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = Mailbox_serializer


class Email_list(generics.ListAPIView):
    queryset = Email.objects.all()
    serializer_class = Email_serializer


class Template_list(generics.ListAPIView):
    queryset = Template.objects.all()
    serializer_class = Template_serializer


class Email_Create(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = Email_serializer
