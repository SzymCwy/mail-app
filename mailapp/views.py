from .models import Mailbox, Template, Email
from rest_framework import generics
from .serializers import Mailbox_serializer, Email_serializer, Template_serializer


class MailboxListCreate(generics.ListCreateAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = Mailbox_serializer


class MailboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = Mailbox_serializer


class EmailListCreate(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = Email_serializer


class TemplateListCreate(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = Template_serializer


class TemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = Template_serializer
