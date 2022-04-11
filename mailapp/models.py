import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Mailbox(models.Model):
    host = models.CharField(max_length=50)
    port = models.IntegerField()
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_from = models.CharField(max_length=50)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now())
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email_from

    @property
    def sent(self):
        return Email.objects.filter(mailbox=self.id).count()


class Template(models.Model):
    subject = models.CharField(max_length=50)
    text = models.TextField()
    attachment = models.FileField(blank=True)
    date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject} - {self.date}'


class Email(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    mailbox = models.ForeignKey(Mailbox, to_field='id', on_delete=models.CASCADE, default=uuid.uuid4)
    template = models.ForeignKey(Template, to_field='id', on_delete=models.CASCADE, default=uuid.uuid4)
    to = ArrayField(models.CharField(max_length=50, blank=False, null=False), blank=False, null=False)
    cc = ArrayField(models.CharField(max_length=50, blank=False, null=False), blank=True, null=True)
    bcc = ArrayField(models.CharField(max_length=50, blank=False, null=False), blank=True, null=True)
    reply_to = models.EmailField(default=None)
    sent_date = models.DateTimeField(default=None, null=True,)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.mailbox} - {self.to}'
