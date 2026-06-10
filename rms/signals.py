from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
import mailtrap as mt
from django.conf import settings




@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
   print("SIGNAL TRIGGERED: New order created.")
   # send_mail(
   #    subject="New Order Created",
   #    message="A new order has been created.",
   #    from_email="signal@example.com",
   #    recipient_list=["user@example.com"],
   # )
   inbox_id = 4426905

   client = mt.MailtrapClient(
      token="Bearer 4addcae338101a029b5f866d6ea663f2",
      sandbox=True,
      inbox_id=inbox_id
   )

   mail = mt.Mail(
      sender=mt.Address(email="admin@email.com", name="Test Sender"),
      to=[mt.Address(email="user@email.com", name="Test User")],
      subject="Order Email",
      text="New Order Has been created.",
      html="<p>This is a <b>test email</b> for sandbox.</p>"
   )

   client.send(mail)