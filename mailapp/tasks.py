from celery import shared_task
from django.core import mail


@shared_task
def send_mail(email):
    mailbox_data = email.get('mailbox')
    template_data = email.get('template')
    try:
        with mail.get_connection(
                host=mailbox_data.host,
                port=mailbox_data.port,
                username=mailbox_data.login,
                password=mailbox_data.password,
                use_tls=mailbox_data.use_ssl
        ) as connection:
            mail.EmailMessage(
                template_data.subject, template_data.text, mailbox_data.email_from, email['to'],
                cc=email['cc'], bcc=email['bcc'], connection=connection,
            ).send()
        return True
    except:
        return False
