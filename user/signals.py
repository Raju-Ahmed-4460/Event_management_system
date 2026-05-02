from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from event.models import Participant, Event
from threading import Thread


def send_event_email(email, subject, message):
    try:
        send_mail(
            subject,
            message,
            "rajur20m@gmail.com",
            [email],
            fail_silently=True
        )
    except Exception as e:
        print("Email error:", e)


@receiver(m2m_changed, sender=Participant.events.through)
def notify_participant_for_event(sender, instance, action, pk_set, **kwargs):

    if action == "post_add":

        event_names = Event.objects.filter(id__in=pk_set).values_list("name", flat=True)
        all_event = ", ".join(event_names)

        subject = "Event Message"
        message = f"You have been selected for: {all_event}"

        Thread(
            target=send_event_email,
            args=(instance.email, subject, message)
        ).start()