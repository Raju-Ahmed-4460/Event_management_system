


from django.db.models.signals import post_save,post_delete,pre_save,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from event.models import Participant,Event,Category


@receiver(m2m_changed, sender=Participant.events.through)
def notify_participant_for_event(sender, instance, action, pk_set, **kwargs):

    if action == "post_add":
        all_mail = [instance.email]  
        all_event=""
        for e in instance.events.all():
            all_event+=e.name+" ,"
        all_event = all_event.rstrip(", ")

        send_mail(
            "Event message",
            f"You have been selected for this{all_event}",
            "rajur20m@gmail.com",
            all_mail,
        )