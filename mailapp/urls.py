from django.urls import path
from .views import MailboxListCreate, MailboxDetail, EmailListCreate, TemplateListCreate, TemplateDetail


urlpatterns = [
    path('mailbox/', MailboxListCreate.as_view()),
    path('mailbox/<int:pk>/', MailboxDetail.as_view()),
    path('email/', EmailListCreate.as_view()),
    path('template/', TemplateListCreate.as_view()),
    path('template/<int:id>/', TemplateDetail.as_view()),
]
