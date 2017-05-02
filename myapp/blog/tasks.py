from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

@shared_task
def convert_to_pdf(instance):
	print "calling convert_to_pdf()..."

	print instance.id
	print instance.title

	# disini nanti ada kode buat convert ke pdf dari artikel yang diubah atau ditambah

	doc = SimpleDocTemplate("assets/pdf/"+instance.title+"_"+str(instance.id)+".pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
	Story=[]
	logo = "python_logo.png"
	magName = "Pythonista"
	issueNum = 12
	subPrice = "99.00"
	limitedDate = "03/05/2010"
	freeGift = "tin foil hat"
	formatted_time = time.ctime()
	full_name = "Mike Driscoll"
	address_parts = ["411 State St.", "Marshalltown, IA 50158"]

	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	ptext = '<font size=20>%s</font>' % instance.title

	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(1, 12))

	ptext = '<font size=10>created  by %s at %s</font>' % (instance.author.username, instance.created_at)

	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(1, 24))

	ptext = instance.body
	Story.append(Paragraph(ptext, styles["Justify"]))
	Story.append(Spacer(1, 12))

	doc.build(Story)

	return True

@shared_task
def send_random_article():
	print "calling send_random_article()..."

	send_mail(
	    'Simak Artikel Pilihan Kami hanya di Today Fake News!',
	    """
	    Hi, Pembaca yang budiman.

	    Lorem ipsum sit dolor amet hahahahhaha.

	    Salam,

	    Today News.
	    """,
	    'today@fakenews.com',
	    [
	    	'mikailsonanjaya@example.com',
	    	'jayarikodan@example.com',
	    	'karimin@example.com',
	    ],
	    fail_silently=False,
	)

	return True

