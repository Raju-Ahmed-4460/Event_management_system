from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from threading import Thread


def send_activation_email_task(user):
    token = default_token_generator.make_token(user)
    activation_url = f"{settings.FRONTEND_URL}/user/activate/{user.id}/{token}/"

    subject = "Activate your account"
    message = f"""
Hi {user.username},

Activate your account by clicking below:
{activation_url}

Thank you
"""

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False
        )
    except Exception as e:
        print(f"Failed to send mail {user.email}: {str(e)}")


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        # ✅ run email in background (fix slow signup)
        Thread(target=send_activation_email_task, args=(instance,)).start()


@receiver(post_save, sender=User)
def assign_role(sender, instance, created, **kwargs):
    if created:
        user_group, _ = Group.objects.get_or_create(name='User')
        instance.groups.add(user_group)