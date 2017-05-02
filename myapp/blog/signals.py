from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Posts
from .tasks import convert_to_pdf

import json

@receiver(post_save, sender=Posts)
def call_pdf_converter(sender, instance, *args, **kwargs):

	print "call_pdf_converter..."

	convert_to_pdf.delay(instance)

	return True
