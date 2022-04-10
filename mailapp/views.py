from .models import Mailbox, Template, Email
from rest_framework import generics
from .serializers import Mailbox_serializer, Email_serializerCreate, Template_serializer, EmailList
from django_filters import rest_framework as filters
from .filters import EmailFilter


class MailboxListCreate(generics.ListCreateAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = Mailbox_serializer


class MailboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = Mailbox_serializer


class EmailCreate(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = Email_serializerCreate


class TemplateListCreate(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = Template_serializer


class TemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Template.objects.all()
    serializer_class = Template_serializer


class EmailListView(generics.ListAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailList
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmailFilter
