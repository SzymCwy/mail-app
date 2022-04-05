from django.shortcuts import render
from .models import Mailbox, Template, Email
from rest_framework import generics
from .serializers import Mailbox_serializer

# Create your views here.


class Mailbox_list(generics.ListAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = Mailbox_serializer
