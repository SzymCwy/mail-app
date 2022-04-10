from django.urls import path
from .views import MailboxListCreate, MailboxDetail, EmailCreate, TemplateListCreate, TemplateDetail, EmailListView


urlpatterns = [
    path('mailbox/', MailboxListCreate.as_view()),
    path('mailbox/<int:pk>/', MailboxDetail.as_view()),
    path('email/create/', EmailCreate.as_view()),
    path('email/', EmailListView.as_view()),
    path('template/', TemplateListCreate.as_view()),
    path('template/<int:pk>/', TemplateDetail.as_view()),
]
