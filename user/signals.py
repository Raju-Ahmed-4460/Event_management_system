from django.db.models.signals import post_save,post_delete,pre_save,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail



@receiver(post_save,sender=User)

def send_activation_email(sender,instance,created,**kwargs):
    if created:
        token=default_token_generator.make_token(instance)
        activation_urls=f"{settings.FRONTEND_URL}/user/activate/{instance.id}/{token}/"

        subject='active your account'
        message=f"Hi {instance.username},\n\n activate your account by clicking the link below\n{activation_urls}\n\n Thank You"
        recipent_list=[instance.email]
        try:
            send_mail(subject,message,settings.EMAIL_HOST_USER,recipent_list)
        except Exception as e:
            print(f"failed to send mail {instance.email}:{str(e)}")
        
